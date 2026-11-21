# Leeds Guide

A mobile web app (PWA) for independent Leeds: places to eat and drink, Victorian arcades, Kirkgate Market, record shops, second-hand gear, vintage, museums, gigs, sport and Yorkshire day trips. Every place has links to Google reviews, TripAdvisor, its own website where it has one, and walking directions in Apple Maps or Google Maps, plus a built-in map.

It's a plain static site with no build step needed to host it. To change the content, edit `build/places.py`, `build/content.html` or `build/info.js`, then run `python3 build/kit/make.py`.
