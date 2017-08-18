import requests

def url(path):
    return 'http://34.207.10.230:3000' + path


def view_feed():
    resp = requests.get(url('/posts'))
    print(resp.content)


def add_news():
    title = input("Enter News Title  '': ")
    body = input("Enter News  Body'': ")
    return requests.post(url('/posts'), json={
        'title': title,
        'body': body
    })


def comment():
    postId = input("Enter News Feed Post Id Between '': ")
    body = input("Enter News Feed Comment Between '': ")
    return requests.post(url('/comments'), json={
        "body": body,
        "postId": postId
    })


def display_menu():
    print("")
    print("----------------------------------------")
    print("Welcome To The TEAM 1 NEWS APP ! :")
    print("")
    print("Select An Option")
    print("")
    print("1. View News Feeds")
    print("2. Post A News Feed")
    print("3. Comment On News Feed")
    print("")


def get_menu_choice():
    print("")
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected : "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print ("Please Re-Enter a valid option")
        except ValueError:
            print ("Please Re-Enter a valid option")
        return choice


def main():

    no_exit = True
    while no_exit:
        display_menu()
        option = get_menu_choice()
        print ("")
        if option == 1:
            view_feed()
        elif option == 2:
            add_news()
        elif option == 3:
            comment()
            print("")
        elif option == 0:
            no_exit = False
            print ("Thank you")
            print ("")

if __name__ == '__main__':
    main()
