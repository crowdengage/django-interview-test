# eventr 

Welcome to eventr, the (fictional) Future of Listings for the Web 3.0 era. Development has just started but 
eventr aims to provide a unified listings API for events at partner venues. All partner venues will use the
Spektrix ticketing system to start with.

eventr aims to add hundreds of partners to its listing portal rapidly, and prides itself on its responsive and 
performant user interface and APIs. Some partners may have just one production with hundreds or thousands of 
performances, while others may have hundreds of productions with only one performance each.

## Terminology

A `Source` is a source of data (i.e. a partner venue's ticketing system).

An `Event` is a particular production, for example "Hamlet".

An `EventInstance` is a performance of a `Event`, for example the Wednesday matinee for Hamlet.

## Tasks

1. Clone this repository (please don't use Github to fork it otherwise it'll be too easy for others to find your solution!)

2. Add the `Source` model to Django admin so that you can easily add new sources. For testing purposes, you may wish to use the following Spektrix clients. 

| Partner Name                  | Spektrix Client Name | Spektrix API help page                                 | Spektrix API "Events" endpoint                           |
| ----------------------------- | -------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Topping & Company Booksellers | toppingbooks         | https://system.spektrix.com/toppingbooks/api/v3/help   | https://system.spektrix.com/toppingbooks/api/v3/events   |
| Mercury Theatre               | mercurytheatre       | https://system.spektrix.com/mercurytheatre/api/v3/help | https://system.spektrix.com/mercurytheatre/api/v3/events |

3. Create a Django management command to sync events and event instances from partner ticketing systems and 
create/update them in the eventr database, using the models in the `listings` app. This management command will be
run manually by eventr staff to start with, but you should make sure that nothing unexpected will happen if two
staff members run the management command at the same time.

4. Using Django REST Framework, create views to allow the listings to be searched/browsed. Users will want to search 
by a combination of the following parameters:
	- event name (partial)
	- partner
	- event instances within date range
	- city (NB: there is no field for City in the Spektrix API response but you can assume that all performances from a single Source will be in the same city)

5. Create a Vue app which displays listings based on those views. The homepage should display events happening across all partner venues.

6. Publish your code on Github as a private repository and add us to it.

## Guidelines

This doesn't have to be production-ready and you can take shortcuts that make sense in the context of a 
fictional project (although we do want to be able to get a sense for your coding style, so don't take 
too many). We may discuss the approaches you've taken (as well as things you might change
in the future or if you had to scale eventr) at interview. There are bonus points available for good 
git ettiquette.
