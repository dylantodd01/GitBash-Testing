from operator import itemgetter
import requests

# Make an API call, store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	# Make a seperate API call for each submission
	url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
	r = requests.get(url)
	print(f"{submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()
	

	# Build a dictionary for each article
	try:
		submission_dict = {
			'title': response_dict['title'],
			'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
			'comments': response_dict['descendants'],
		}
	except KeyError:
		submission_dict = {
			'title': response_dict['title'],
			'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
			'comments': 0,
		}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, comments = [], []
for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")

	titles.append(submission_dict['title'])
	comments.append(submission_dict['comments'])



# Plot the submissions
from plotly.graph_objs import Bar
from plotly import offline

data = [{
	'type': 'bar',
	'x': titles,
	'y': comments,
	'marker': {
		'color': 'rgb(0, 150, 200)',
		'line': {'width': 1.5, 'color': 'rgb(10, 10, 10)'}
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Most-Commented Submissions on Hacker News',
	'titlefont': {'size': 28},
	'xaxis': {
	'title': 'Submission Title',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14},
	},
	'yaxis': {
	'title': 'No. Comments',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')