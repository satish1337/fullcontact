import sys, fullcontacter




FC_API_KEY= ""

def main():
    if len(sys.argv) is 3:
        if sys.argv[1] == "-e":
            fc(sys.argv[2], "email")
        elif sys.argv[1] == "-t":
            fc(sys.argv[2], "twitter")
        else:
            print "Invalid Arguments"
    else:
        print "Insufficent Arguments"

def fc(key, key_type):
    fc_person = fullcontacter.personLookup(FC_API_KEY)
    response = fc_person.lookitup(key, key_type)
    if response["status"] == 200:
        response = format_response(response)
        print_response(response)
    else:
        print "No results found"

def format_response(response):

    contact_info = response["contactInfo"]["fullName"]
    social_profiles = [dict(website = item["typeName"], url = item["url"]) for item in response["socialProfiles"]]
    results = dict(name = contact_info, social_profiles = social_profiles)
    return results

def print_response(response):
    print "Name: " + response["name"]
    for item in response["social_profiles"]:
        print item["website"] + ": " + item["url"]


if __name__ == "__main__":
    main()
