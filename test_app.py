import unittest
import json
from application import create_app
from models import setup_db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql.expression import func, select


class CapstoneTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone-test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(app=self.app, db_path=self.database_path)
        self.casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iml2a09JR1YxVnZwUEVpTVN0MTl0YSJ9.eyJpc3MiOiJodHRwczovL2ZzZG5kLWFsYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjdhMjk3YjZkNzUyMDA2OGVhNTAyZiIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjIzMTY4MjUxLCJleHAiOjE2MjMyNTQ2NTEsImF6cCI6Ilo2Rk5GT1dtOVlvYmVHUm56UzF5QkJyZU80cEQ5RktLIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.Ff0rqajqJroVOxBCkbZstIq16uYLgWifhIoYozi4VBybhD0n1bZFo8NwMMKA7_A4N25mZ-pQHD6xVC-k9zvwozsPYwYhRHOmMweJyC2_L6u1PmmSzKZjPzoQ3oDzdHSu-kBzIX1xmklsBvV0EYKIgQwiSTkW_Kvik7fl3-JKecSSVxUHIVChv0DkiUqC8YOb8VRL3RVJK6xqaXXa04LDQdJWJTzxYq2tr1puRKg8va6_texibGqHn1uxK6H8kEqdeS3S1IBmWuxXA9McQKmfcSb2m2HW8zb3IV4YsjgfpSD3NrS_hKjPmm_-DGPTdLeJYDX1ERPMXpJ4hLXr-4njfg'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iml2a09JR1YxVnZwUEVpTVN0MTl0YSJ9.eyJpc3MiOiJodHRwczovL2ZzZG5kLWFsYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjdhNWVhMzhkNDlhMDA2OTJiM2JkOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjIzMTY4NDAyLCJleHAiOjE2MjMyNTQ4MDIsImF6cCI6Ilo2Rk5GT1dtOVlvYmVHUm56UzF5QkJyZU80cEQ5RktLIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.AMSvpUWCS7EqTqfBKF4ErqannY2mIah89cNSLFgcqDSgsHCxxEfV7UzJm1V8j4Y1GBPgR4YXdDf7vxBf53bk6SNV7mz0OxR10AOgoNRKBTvMDYo6w-oxZssX1nmlxWaq8vkyV_AsoO59NtuQuOdMQUlaqqcCuYKdHl0lnq8DxIl3GV-8XV6Eu6x_gg9KWGz3G7a0UOHDulCrXwPjv3MO__2aunOmEPo41rQtA8MUtO7KAEJj_Vs9IJp_eseUTeY-mfVl2-Oc3ZZePre6eGk9bIVandlcbhod4HSHfEqg6REIna1iWq0StaG_Z6FKZmbkLQLPNKlmBsGIDuUfjZ-Z7A'
        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iml2a09JR1YxVnZwUEVpTVN0MTl0YSJ9.eyJpc3MiOiJodHRwczovL2ZzZG5kLWFsYW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjdhY2E2NmI3MTg2MDA2OWMzZTkwNyIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNjIzMTY4NDgxLCJleHAiOjE2MjMyNTQ4ODEsImF6cCI6Ilo2Rk5GT1dtOVlvYmVHUm56UzF5QkJyZU80cEQ5RktLIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.23A6gmoqLJL2u1r4hlkK3gMZZKoz5Rvz1K_3EFjnMbNWwZ2Gb6DepHsUUzMPWt7Xyt1mt1hvkPQHkHLRCadAJe_QWO_SnfrWlYnueqy8bikIz91uRhcD5KZZoL5ZUZiUfSHFEREEZfSBFoPAtwfPZaU60p5sULh8SbiK7vXkFVaraRTZdTXpCHlxhtxTd4bOMyZ4IECndGvJYefHLR4fi-iIR2LehItiJwK_x29eJA8QkMzfWczcMbsULngLVZIIEFM9O8XkOpfhI72ZAeq_xUHsngIQZMSLrVhOrJz2T9vdy1r8uTl_9sfio56_7EMqQrsrvntrtOBy0J8Enf_LRA'
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    # ---------------------------------------------------------------
    # No Auth
    # ---------------------------------------------------------------

    def test_get_home(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_actors(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)

    # ---------------------------------------------------------------
    # Casting assistant
    # ---------------------------------------------------------------

    def test_get_actors_ca(self):
        res = self.client().get('/actors',
                                headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_get_movies_ca(self):
        res = self.client().get('/movies',
                                headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_post_actor_ca(self):
        sent = {'age': 25,
                'gender': "Male",
                'name': "Example"}
        res = self.client().post('/actors',
                                 headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)},
                                 json=sent)
        self.assertEqual(res.status_code, 401)

    def test_post_movie_ca(self):
        sent = {'title': 'Example',
                'release_date': datetime.today()}
        res = self.client().post('/movies',
                                 headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)},
                                 json=sent)
        self.assertEqual(res.status_code, 401)

    def test_update_actor_ca(self):
        sent = {
            'name': 'Updated'
        }
        res = self.client().patch('/actors/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)},
                                  json=sent)
        self.assertEqual(res.status_code, 401)

    def test_update_movie_ca(self):
        sent = {"title": "Example"}
        res = self.client().patch('/movies/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)},
                                  json=sent)
        self.assertEqual(res.status_code, 401)

    def test_delete_actor_ca(self):
        res = self.client().delete('actors/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)})
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_ca(self):
        res = self.client().delete('/movies/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.casting_assistant_token)})
        self.assertEqual(res.status_code, 401)

    # ---------------------------------------------------------------
    # Casting director
    # ---------------------------------------------------------------

    def test_get_actors_cd(self):
        res = self.client().get('/actors',
                                headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_get_movies_cd(self):
        res = self.client().get('/movies',
                                headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_post_actor_cd(self):
        sent = {'age': 25,
                'gender': "Male",
                'name': "Example"}
        res = self.client().post('/actors',
                                 headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)},
                                 json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_post_movie_cd(self):
        sent = {'title': 'Example',
                'release_date': datetime.today()}
        res = self.client().post('/movies',
                                 headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)},
                                 json=sent)
        self.assertEqual(res.status_code, 401)

    def test_update_actor_cd(self):
        sent = {
            'name': 'Updated'
        }
        res = self.client().patch('/actors/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)},
                                  json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_cd(self):
        sent = {"title": "Example"}
        res = self.client().patch('/movies/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)},
                                  json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_cd(self):
        res = self.client().delete('actors/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_cd(self):
        res = self.client().delete('/movies/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.casting_director_token)})
        self.assertEqual(res.status_code, 401)

    # ---------------------------------------------------------------
    # Executive producer
    # ---------------------------------------------------------------

    def test_get_actors_ep(self):
        res = self.client().get('/actors',
                                headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    def test_get_movies_ep(self):
        res = self.client().get('/movies',
                                headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])

    def test_post_actor_ep(self):
        sent = {'age': 25,
                'gender': "Male",
                'name': "Example"}
        res = self.client().post('/actors',
                                 headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)},
                                 json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_post_movie_ep(self):
        sent = {'title': 'Example',
                'release_date': datetime.today()}
        res = self.client().post('/movies',
                                 headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)},
                                 json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_update_actor_ep(self):
        sent = {
            'name': 'Updated'
        }
        res = self.client().patch('/actors/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)},
                                  json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_ep(self):
        sent = {"title": "Example"}
        res = self.client().patch('/movies/1',
                                  headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)},
                                  json=sent)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_ep(self):
        res = self.client().delete('actors/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_ep(self):
        res = self.client().delete('/movies/2',
                                   headers={'Authorization': 'Bearer {}'.format(self.executive_producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
