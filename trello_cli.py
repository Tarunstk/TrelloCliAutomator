import pip._vendor.requests as requests
import json
import argparse

endpoint = "https://api.trello.com/1" #base endpoint for trello.com

#function to create a card on a list
def create_card(key, token, idList, name, desc, idLabels):
    
    card_endpoint = endpoint+"/cards" #adding the endpoint information for the card based on the api documentation

    query = {"key":key,"token":token,"idList":idList,"name":name,"desc":desc,"idLabels": ','.join(idLabels)}

    response = requests.post(card_endpoint, params = query) #POST operation to create card based on query parameters
    if response.status_code == 200:
        card = response.json()
        print("Card creation successful!") 
        print("CardId for the newly creatd card is:", card['id'])

    else:
        print("Request could not be completed",response.text) #if response code is not 200 then there is an error

    
    
#function to add a comment onto a card based on the cardId
def create_comment(key, token, cardId, comment):

    comment_endpoint = endpoint+"/cards/"+cardId+"/actions/comments" #adding the endpoint information for the comment based on the api documentation

    query = {"key":key,"token":token,"id":cardId,"text":comment}
    response = requests.post(comment_endpoint, params = query) #POST operation to add comment based on query parameters
    if response.status_code == 200:
        print("Comment posted successfully!")
    else:
        print("Request could not be completed",response.text) 
   
#main method
def main():
    #argparse module has been used to include a Command Line Interface into the application. 
    parser = argparse.ArgumentParser(description = 'Welcome to the trello automator. Create cards and post comments with just one line.')
    subparsers = parser.add_subparsers(dest = 'command')
    #adding positional argument create_card and the flags. 
    card_parser = subparsers.add_parser('create_card')
    card_parser.add_argument('key', help = 'This will be your generated api key for trello.com')
    card_parser.add_argument('token', help = 'This will be your generated token key for trello.com')
    card_parser.add_argument('idList', help = 'The id of the list you want the card added to')
    card_parser.add_argument('name', help = 'The name of the card')
    card_parser.add_argument('desc', help = 'The description of the card')
    card_parser.add_argument('--idLabels', nargs='*', help='the id labels of the cards you wan to add') #adds labels to your card, optional flag. 

    #adding positional argument create_comment 
    comment_parser = subparsers.add_parser('create_comment')
    comment_parser.add_argument('key', help = 'This will be your generated api key for trello.com')
    comment_parser.add_argument('token', help = 'This will be your generated token key for trello.com')
    comment_parser.add_argument('cardId', help = 'The id of the card you want the comment in')
    comment_parser.add_argument('comment', help = 'The content of the comment')
    
    arg = parser.parse_args()

    if arg.command == 'create_card':
        create_card(arg.key, arg.token, arg.idList, arg.name, arg.desc, arg.idLabels)
    elif arg.command == 'create_comment':
        create_comment(arg.key, arg.token, arg.cardId, arg.comment)

    #prints the help message
    else: 
        parser.print_help()

if __name__=='__main__':
    main()
