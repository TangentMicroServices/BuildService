from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class ViewsTestCase(TestCase):

	def setUp(self):
		self.c = Client()

	def test_all_views_ok(self):

		pages = [
			('build_ui:project_dashboard', ('some-repo',) ),
			('build_ui:repo_dashboard', ('some-repo',) ),
			('build_ui:smells', ('some-repo',) ),
			('build_ui:leaderboard', None),
			('build_ui:wall_of_shame', None),
			('build_ui:overview_dashboard', None),
		]

		for page, args in pages:
			
			if args is None:
				url = reverse(page)
			else:
				url = reverse(page, args=args)
			
			response = self.c.get(url)
			assert response.status_code == 200, \
				'{} not ok. Content: {}' . format (page, response.content)


