from bs4 import BeautifulSoup
import urllib2
import json
import copy

urls = ["https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=bb70920a-779a-4dd4-827f-edd320211ae9", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=6f60aca9-7fba-4bf1-b6af-1f85e9376462", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=c3b234ff-c492-4df0-90b2-08b95850c9e9", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=51618221-713e-40ee-b133-5003503dd7cf", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=abcbaa33-bfc8-4054-87ca-67c3aa0a6a13", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=bcabbadc-d38e-477d-82f2-4356f4165b71", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=83b48f1e-9afb-4b87-aef8-4c7eba064a41", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=d9b13b32-adc7-47b2-a978-84cf6dfcf976", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=d653a057-0bb3-45f4-be08-0a31035a9021", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=a26cd06f-2f4e-4ec7-b946-0985984ba255", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=bfddec09-d9a6-4915-8aac-f97b28f95d0d", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=3df2fa09-2866-49e3-8526-6705450be265", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=d53bddc9-7289-46a1-b9c2-b676275eeec8", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=9e124956-340b-420b-93db-0ae6ddc570d9", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=22529c27-ba7f-45b9-a331-c9a38d56ef80", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=dc963254-55db-4fa9-bea9-dd54c140a8f5", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=b07d7c18-0546-421d-99f0-4c87e8147d11", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=fc6baae6-87a0-424e-9cd6-e07471e083ea", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=8c1fd57a-b00b-4969-8606-f7effef9260b", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=2da64b66-2f65-4f73-aef5-b992ba8ffdd2", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=5e568875-dadf-47bb-9080-ad4c4df145c1", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=58b4988f-fb79-42f9-bd19-f7dbb6c8eab7", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=b2eacfee-0fad-4fa1-a4bd-609bfe3ca532", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=f8162fb1-c828-431b-a6f8-c1bab9927b61", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=8a7dc020-1b11-40ca-974d-39272427a3b4", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=a3e9c00d-5aa7-45ea-ad73-f62c293856a8", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=5d72208a-069d-4931-aaa6-9527346efc6f", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=4c8a432d-409a-46eb-a1f5-a92bf3b609a2", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=8790ee63-595f-40e9-9735-a325903b186c", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=bf76ecfc-d619-41bf-8e4b-f2158c1b6471", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=64284919-2dd7-4758-bb03-3d632071bd31", "https://nike.uwaterloo.ca/FacilityScheduling/FacilitySchedule.aspx?FacilityId=f30dc951-26b0-4909-b814-ce54d38c2fbb"]
results = []

counter = 1

for url in urls:
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, "html.parser")


	activities = map((lambda x: x.parent), soup.find_all("span", id=lambda x: x and "StartTime" in x))
	location_soup = soup.find("td", class_="dxscHorizontalResourceHeader_Metropolis").contents
	location = location_soup[0].split('>')[-1]

	for activity in activities:
		start_time = activity.find("span", id=lambda x: x and "StartTime" in x).contents[0][:-1]
		end_time = activity.find("span", id=lambda x: x and "EndTime" in x).contents[0]
		name = activity.find("span", id=lambda x: x and "Title" in x).contents[0]
		results.append({
			"start_time": start_time,
			"end_time": end_time,
			"name": name,
			"location": location
			})
	counter = counter + 1

rec_results = filter(lambda result: result and result["name"] and "Rec" in result["name"], results)
def parse_activity(activity):
	activities = ["basketball", "swim", "badminton", "soccer", "multi", "volleyball", "studio", "open"]
	for a in activities:
		if a in activity["name"].lower():
			newobj = copy.copy(activity)
			newobj["name"] = a
			return newobj

	return activity
rec_parsed = map(parse_activity, rec_results)

"""
with open('data.json', 'w') as outfile:
    json.dump(rec_parsed, outfile)
"""

print json.dumps(rec_parsed)
