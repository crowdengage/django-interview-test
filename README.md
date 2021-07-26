# eventr 

Welcome to eventr, the (fictional) Future of Listings for the Web 3.0 era. Development has just started but 
eventr aims to provide a unified listings API for events at partner venues. All partner venues will use the
Spektrix ticketing system.

## Terminology

A `Source` is a source of data (i.e. a partner venue's ticketing system).

An `Event` is a particular production, for example "Hamlet".

An `EventInstance` is a performance of a `Event`, for example the Wednesday matinee for Hamlet.

## Tasks

Please clone this repository and work

1. Add the `Source` model to Django admin so that you can easily add new sources. For testing purposes, you may wish to use the following Spektrix clients:

| Partner Name                  | Spektrix Client Name | Spektrix API help page                                 | Spektrix API "Events" endpoint                           |
| ----------------------------- | -------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Topping & Company Booksellers | toppingbooks         | https://system.spektrix.com/toppingbooks/api/v3/help   | https://system.spektrix.com/toppingbooks/api/v3/events   |
| Mercury Theatre               | mercurytheatre       | https://system.spektrix.com/mercurytheatre/api/v3/help | https://system.spektrix.com/mercurytheatre/api/v3/events |

2. Create a Django management command to sync events and event instances from partner ticketing systems and 
create/update them in the eventr database, using the models in the `listings` app.

3. Using Django Rest Framework, create views to allow the listings to be searched/browsed.

4. Create a Vue app which displays listings based on those views.

Bonus points for good git ettiquette!
