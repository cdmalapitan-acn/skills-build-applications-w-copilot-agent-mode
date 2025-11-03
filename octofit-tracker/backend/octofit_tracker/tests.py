from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel)
        batman = User.objects.create_user(email='batman@dc.com', username='batman', team=dc)
        Activity.objects.create(user=ironman, type='run', duration=30)
        Workout.objects.create(name='Pushups', description='Upper body workout')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        user = User.objects.get(username='ironman')
        self.assertEqual(user.team.name, 'Marvel')

    def test_activity(self):
        activity = Activity.objects.get(type='run')
        self.assertEqual(activity.duration, 30)

    def test_workout(self):
        workout = Workout.objects.get(name='Pushups')
        self.assertEqual(workout.description, 'Upper body workout')

    def test_leaderboard(self):
        leaderboard = Leaderboard.objects.get(team__name='Marvel')
        self.assertEqual(leaderboard.points, 100)
