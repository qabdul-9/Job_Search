import requests
from bs4 import BeautifulSoup
import csv

def main():

    print('''
__        __   _                          _ 
\ \      / /__| | ___ ___  _ __ ___   ___| |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
  \ V  V /  __/ | (_| (_) | | | | | |  __/_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)
        ''')

    url = "https://www.xula.edu/about/mission-values.html"
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers).text
    # response = requests.get(url)
    soup = BeautifulSoup(response, 'html.parser')

    # Extract all links
    for link in soup.find_all('a'):
        print(link.get('href'))
    print(soup.find('div', class_='editorarea').text)

    url = "https://catalog.louisiana.edu/content.php?catoid=21&navoid=7555"
    response = requests.get(url, headers=headers).text
    # response = requests.get(url)
    soup = BeautifulSoup(response, 'html.parser')

    # Extract all links
    for link in soup.find_all('a'):
        print(link.get('href'))
    print(soup.find_all('p'))

    url = "https://www.indeed.com/viewjob?jk=3bc2632e8b136aca&tk=1j7vp1jfcgn3480q&from=hp.jobsForYou&advn=1263317315706253&adid=437267655&ad=-6NYlbfkN0BV_Cmb1x6vTJGFs71wi4-q81fQpW24FBxMuxzT2KlyKV87JKLU_OoRBnU-x9dnGrs0RnLA60CefGPuZPkjeErQVJAVlxRBpsOAhpac9t_XynlSZ-A-D8crd6GvFYLsfvLEmhyzHXmhkmhyOoVx6ICYBqYAeEnK6PeeYqDA76NI7dP_wzrfE87suiGUo4hbCynx_Rc5DvDiTqp9sk2RA-sYrlzJl9QRcn8Q3GP-RcXZ-pDPHbkMvC9yXeGmc2eq20DZRegCdfU1lz469W-nU7SfJjjMgCa4gEY0wEChHnSwsON7KR7-Y58fK4ZFJHRYGrSGNYz6A4E9JSFjDn34Mb0Fwmj7R21qhNRQji7J3nXDelAWrhB-_S7h6ktPbZU87LWWsLmkB1Xt6PuiZs7YcMA-R5UQJrxEIRhE8I5Ll9IBAQfT-h0FlSwhLHrxdZC8i4H6gnK5O_rzL5k6r4jN2NsJ_uaS5l-v6er4OYeE4fEk1ZDYSAyD_afnszACLL6UGX067lMeTqzzZEw2KonXMT73FpsDjuYbFFnUfhlKyuS3s9uc_cbkxC_qGOyUkamjtDMQoLmvjx-04fGrqSe32euxmhitZaExOPN03lCUa9yINbO_c_m5UleNo_jrt4hZ_BE%3D&pub=4a1b367933fd867b19b072952f68dceb&camk=nUmJqO2E8rhVCuD0s2mU2w%3D%3D&xkcb=SoDO6_M3s_6Jq6AQeL0PbzkdCdPP&xpse=SoA76_I3s_9DW2ywGB0PbzkdCdPP&xfps=0825e3d7-9134-4785-ba3c-8ec12c333371&vjs=3"
    response = requests.get(url)

    if response.status_code == 200:
        job_cards = soup.select('div data-testid=')

        for card in job_cards:
            title_element = card.select_one('')
            company_element = card.select_one('')
            location_element = card.select_one('p.location')
            date_element = card.select_one('time')

            title = title_element.text.strip() if title_element else "No Title Found"
            company = company_element.text.strip() if company_element else "No Company Found"
            location = location_element.text.strip() if location_element else "No Location Found"
            date_posted = date_element.text.strip() if date_element else "No Date Found"

        print(f"Job Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"Date Posted: {date_posted}\n")

    else:
        print("Failed to retrieve the webpage, status code:", response.status_code)


    with open("fake_job.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Paragraph'])



if __name__ == "__main__":
    main()