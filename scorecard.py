# import sunlight
from sunlight import congress
# from sunlight.pagination import PagingService

def main():

    representatives = []
    senators = []   
    scores = {}

    # grab bioguides
    print 'Collecting legislators...'
    for (varname, chamber) in ((senators, 'senate'), (representatives, 'house')):
        i = 0
        while True:
            new_reps = congress.legislators(chamber=chamber, fields='bioguide_id', page=i)
            if new_reps is None:
                break
            for nr in new_reps:
                varname.append(nr.get('bioguide_id'))
            i = i + 1
    
    # initialize scores dict
    for legislator in representatives + senators:
        scores[legislator] = {} 


    # sponsor/cosponsor of Surveillance State Repeal Act [hr2818-113] (+4)
    print 'checking sponsor/cosponsors of Surveillance State Repeal Act...'
    bill = congress.bills(bill_id='hr2818-113', fields='cosponsor_ids,sponsor_id')[0]
    sponsor_and_cosponsors_ids = bill.get('cosponsor_ids') + [bill.get('sponsor_id')]
    
    for legislator in scores:
        score = 0
        if legislator in sponsor_and_cosponsors_ids:
            score = 4
        scores[legislator]['sponsor/cosponsor of Surveillance State Repeal Act (+4)'] = score


    # sponsor/cosponsor of Senate version of USA FREEDOM [s1599-113] (+4)
    print 'checking sponsor/cosponsors of Senate version of USA FREEDOM...'
    bill = congress.bills(bill_id='s1599-113', fields='cosponsor_ids,sponsor_id')[0]
    sponsor_and_cosponsors_ids = bill.get('cosponsor_ids') + [bill.get('sponsor_id')]
    
    for legislator in scores:
        score = 0
        if legislator in sponsor_and_cosponsors_ids:
            score = 4
        scores[legislator]['sponsor/cosponsor of Senate version of USA FREEDOM (+4)'] = score


    # voted for House version of USA FREEDOM [hr3361-113] (-3)
    print 'checking votes on House version of USA FREEDOM...'
    votes = congress.votes(bill_id='hr3361-113', fields='voters')
    for legislator in scores:
        score = 0
        if votes[0]['voters'][legislator]['vote'] == 'Aye':
            score = -3
        scores[legislator]['voted for House version of USA Freedom (-3)'] = score

    
    # sponsor/cosponsor of FISA Improvements Act [s1631-113] (-4)
    print 'checking sponsor/cosponsors of FISA Improvements Act...'
    bill = congress.bills(bill_id='s1631-113', fields='cosponsor_ids,sponsor_id')[0]
    sponsor_and_cosponsors_ids = bill.get('cosponsor_ids') + [bill.get('sponsor_id')]
    
    for legislator in scores:
        score = 0
        if legislator in sponsor_and_cosponsors_ids:
            score = -4
        scores[legislator]['sponsor/cosponsor of FISA Improvements Act (-4)'] = score


    # cosponsored House version of USA Freedom on or before 5/18/2014 (+3)
    # Conyers-Amash Amendment (vote +4)
    # Rogers Bill (cosponsor -4)
    # Reauthorizing Section 215 of the Patriot Act (vote(?) -.5)
    # Reauthorizing FISA Amendments Act (vote(?) -.5)
    


if __name__ == '__main__':
    main()