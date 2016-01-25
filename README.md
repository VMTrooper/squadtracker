SquadTracker
=============
Side project to keep track of video game teammates for games that provide an API (ex: Bungie's Destiny)

## Testing
### Functional Tests
	python3 manage.py test --liveserver=staging.squadtracker.io functional_tests
	python3 manage.py test --liveserver=staging.squadtracker.io functional_tests.test_simple_list_creation
	python3 manage.py test --liveserver=staging.squadtracker.io functional_tests.test_layout_and_styling
	python3 manage.py test --liveserver=staging.squadtracker.io functional_tests.test_list_item_validation

### Unit Tests
	python3 manage.py test --liveserver=staging.squadtracker.io destiny
	python3 manage.py test --liveserver=staging.squadtracker.io destiny.tests.test_views
	python3 manage.py test --liveserver=staging.squadtracker.io destiny.tests.test_models