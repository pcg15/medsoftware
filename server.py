def main():

    import requests
    r1 = requests.get("http://bme590.suyash.io/list")
    print(r1)
    r2 = requests.post("http://bme590.suyash.io/student",
                       json={"first_name": "Chace", "last_name": "Gore",
                             "netid": "pcg15", "github_username": "pcg15",
                             "team_name": "CPS"})
    r3 = requests.post("http://bme590.suyash.io/sum", json={"a": 1, "b": 2})
    sum_result = r3.json()
    print("The response was {0}.".format(sum_result['result']))

if __name__ == '__main__':
    main()
