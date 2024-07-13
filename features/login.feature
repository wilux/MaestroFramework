Feature: User log ins

#@ios
    Scenario Outline: Credit User sees Credit Login
        Given The user open Stori App
        When The user logins with <user_email> and <password>

        Examples:
            | user_email                 | password   |
            | stori.pruebam1@yopmail.com | Holamundo1 |
#            | storicore.test82@yopmail.com |Holamundo1|
#            | stori.prueba1549@yopmail.com |Holamundo1|
