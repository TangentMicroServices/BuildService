import random
from django.shortcuts import render

def get_status(value, thresholds, higher_is_better=True):
	
	if higher_is_better:
		if value < thresholds[0]: return 'danger'
		if value < thresholds[1]: return 'warning'
		return 'success'
	else:
		if value < thresholds[0]: return 'success'
		if value < thresholds[1]: return 'warning'
		return 'danger'

def dashboard(request):
	context = {}
	return render(request, 'ui/dashboard.html', context)

def project_dashboard(request, project):
	context = {}
	return render(request, 'ui/project_dashboard.html', context)

def repo_dashboard(request, repo):

	qty = random.choice(range(0,100))
	cov = random.choice(range(0,100))
	rem = random.choice(range(0,10000000))
	iss = random.choice(range(0,3000))

	booleans = [
		("build_passed", random.choice([True, False])),
		("has_static_analysis", random.choice([True, False])),
		("has_tests", random.choice([True, False])),		
	]

	key_metrics = [
		{
		 "name": "Quality", 
		 "value": qty, 
		 "type": "percent", 
		 "status": get_status(qty, thresholds = [30, 60])
		},
		{
		 "name": "Test Coverage", 
		 "value": cov, 
		 "type": "percent", 
		 "status": get_status(cov, thresholds = [30, 60])},
		{
		 "name": "Remediation", 
		 "value": rem, 
		 "status": get_status(rem, thresholds = [1000, 1000000], higher_is_better=False)
		 },
		{
		 "name": 
		 "Issues", 
		 "value": iss,
		 "status": get_status(iss, thresholds = [1000, 2000], higher_is_better=False)},
	]

	build_history = []
	for x in range (1,20):
		build_history.append({"status": random.choice(['SUCCESS', 'FAIL']) })
	
	context = {
		"section_title": "Repository", 
		"page_title": "Some Repo",
		"key_metrics": key_metrics,
		"ui_state": ['success', 'warning', 'danger'], 
		"build_history": build_history,
		"booleans": booleans,
	}
	return render(request, 'ui/repo_dashboard.html', context)

def leaderboard(request):
	context = {}
	return render(request, 'ui/dashboard.html', context)

def wall_of_shame(request):
	context = {}
	return render(request, 'ui/dashboard.html', context)

def smells(request, repo):
	context = {}
	return render(request, 'ui/dashboard.html', context)