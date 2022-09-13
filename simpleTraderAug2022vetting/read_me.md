******
Copyright (C) 2022 Truth Malachi Foreman <truthmf@gmail.com>
******
This file is part of the simpleTraderAug2022vetting project.
formatted review and comments to this file is linked here https://docs.google.com/document/d/1B6N9VqN1m1NMyw6ur420shvZhu_6N_QKUNdipV4VHfo/edit?usp=sharing
This file is updated laggardly to that file.
******
simpleTraderAug2022vetting and all associated files and directories within can not be copied and/or distributed without the express written permission of Truth Foreman.
******
DISCLAIMER
!!!IMPORTANT!!! THE INFORMATION IN THIS DIRECTORY AND ITS CHILDREN DIRECTORIES AND FILES ARE TO BE TAKEN AS IS AND DO NOT REPRESENT FINANCIAL OR LEGAL ADVICE. 

This is the read_me.txt file for the simpleTraderAug2022vetting project.
The following listed files and directories are written and annotated exclusively by Truth Malachi Foreman.
Please schedule a meeting with me Truth Foreman via phone or email to receive a detailed explanation of their utility, execution, and development. Feel free to privately comment and review these files on your Google drive.
Please do not link directly to files as they may be replaced or updated periodically. Comments may also be lost during updates. If you wish to preserve comments please keep them separate.
4193670647
Truthmf@gmail.com

Folders/directories
./simpleTraderAug2022vetting/
tf_analysis_bazinga_shortened.py (couple hundred lines of code)
Description: Run this script to see if the input stock symbols have a buy-long or sell-short ”hammer” and or news sentiment signal on them at the daily timeframe. A trading idea/recommendation is then to trade according to the signal with a greater than 1 take profit to stop loss ratio.
The Signaling Timeframe and symbols may be changed at the bottom of the file
This small program was written the week of August 22nd 2022
Instructions :
Download the folder simpleTraderAug2022vetting
Open any command line that has Python3 installed 
Change to the directory where you have the folder downloaded
From command line type “pip install -r requirements.txt” and run/press-enter
From the command line type “python3 tf_analysis_bazinga_shortened.py” and run/press-enter
Wait no more than a minute for the program to execute and say “done”
Browse and use the displayed information as you wish
tf_analysis_bazinga_shortened.ipynb
Description: the function is similar to the above .py file except you will be able to manipulate the data after producing it. Over zoom I can use this file to show you what else I might develop from the data in real time, as well as different ways to browse and package it for use elsewhere. 
I can show you:
 how I would programmatically send the alerts via email
Automate trades (for options or stock)
Make a copy trader using TDAmeritrade accounts



Additional unsolicited information about me below the following line



Additional code examples and projects are available with limited viewing via zoom to protect the intellectual property rights of Truth Foreman and include but are not limited to the following:
Projects (please note many of these projects are under development or dormant and may or may not be annotated properly and may have as many as thousands of lines of codes) (projects start from 2017 onward)
Benzinga analyst price targets API automated trader 
Access and trade position maker Complete but missing trade executor
TDA per second (or any timeframe) Optionchain aggregator
Price history backup 
Trade strategy backtesters
Elliot wave finder 
wedges and channels finder incomplete
Multi double smoothed stochastic oscillator signal trader
TDA email alerts trade automator
Implied volatility convul
Other multi signal confirmation signallers 
RSI pattern finder and signaler
Remote forex trader (incomplete)
Coinbase pro API trade strategiser and automated trader (incomplete)
Instagram Automation bot(dormant since 2019)
Membership Service website for buying a bot(incomplete)
Personal journal website(incomplete)
Personal freelance services signup website (incomplete) 
Fully customized React ux Apparel E-commerce website connecting to Shopify business backend
Social information networking app (intuitive data organization app)(incomplete)
React native

My knowlwedge:
My development workflow:
Environment:
I program in 
Python3, C, CPP, JS, HTML, Swift, CSS, MatLab, MQL, 
Public/proprietary Framework, Formula, library usage and familiarity examples (list not extensive):
Node, React, React-native, Shopify-Liquid, Flask, Django, Plotly, matplotlib, Microsoft Excel, Pandas, Numpy, Scipy, 0MQ
Services knowledge:
AWS (all), WordPress, Shopify, Stripe, MONGODB, SQL, Google Ads, Google Analytics, Facebook and IG Ads, ThinkOrSwim, Docker-Kuberneates, 
Abilities:
some network communications, basic language processing and sentiment analysis, complex math algorithm implementations, solid statistics and probability implementation and explanation
I’m learning:
JAVA, .NET, Kotlin, Dart/Flutter, GoLang, Vue, Ruby
I use finder, iCloud, google-drive, gmail, terminal, visual studio code, and jupyterLabs on macOS(desktop)
Especially For computationally intensive executions like backtests and database indexing
I use files, iCloud, Google-drive, pyto, carnets plus (jupyterNotebooks) on iOS(mobile)
For on the go development
Production workflow
I use Google-drive and or AWS for hosting and sharing projects 
Cloud9, S3 for hosting development projects
S3, Elastic BeanStalk, DynamoDB, and API Gateway for creating publicly accessible services

My review and feedback on Benzinga and Benzinga Pro Services
Red means important to me
Blue means I have a solution / I would like to improve it
Review
App
Why is the web experience so much more different (and comprehensive… especially for access to training and trial resources)  than the app?
Symbol chart/dashboard
Unusual placement for creating new watchlist from chart view
Add “done” button or change top bar text to “search watchlists” which better reflects its functionality 
Move to below notifications notch
What is zingernation tab?
No access to deeper analysis on analyst and their ratings from analyst ratings tab
Tap to access success rate, recent successful ratings, comparison to other analyst, rating progress, etc.
No tab for special signals and alerts via Benzingas special made services? I.e. unusual options alerts and technical analysis
Alerts tab
Need ability to turn on different kinds of alerts for watchlist 
Unusual options
Technical analysis signals
Website https://pro.benzinga.com/dashboard
Mobile
Desktop
It feels like the onboarding-checklist-module popped up one day but was gone the next and then popped up again just recently after me not being able to find it
I find this module of high value in regards to adapting to all of the apparent services on the dashboard and the services advertised elsewhere
General
Unusual options activity table : https://www.benzinga.com/calendars/unusual-options-activity
the table could have a lot more useful properties/columns per alert which the user should be able to turn on and off depending on their preference:
Average daily volume for the past k days (i.e. 21 days)
Average daily open-interest for the past k days (i.e. 21 days)
Average daily volume/open-interest ratio for the past k days (i.e. 21 days)
Could the alerts have recommended-trade-activity / copy-trade button for paid users?
The definitive difference between the day volume and the trade volume is a little ambiguous 
My assumption is that trade volume is a representation of the contract volume for the day and day volume is the whole option-chain volume for the for the day ( or for the strike across all expiration dates… or for all strikes on the same expiration date )
Multiple column sorting
What does a red/green/white background represent in the strike price column
What does a negative DTE mean?
The table seems to only show trades alerts 15 minutes around market close. Is this accurate functionality?
Trading school https://www.benzinga.com/plus/school
instructor/class side-bar-selection-menu does not scroll (looks like theres a class selection i can not reach)
General
Why can’t edu.benzinga.com and Benzinga.com use the same login?
I can write a solution to sync user pools using AWS Cognito and AWS Federations or using whatever your user management system is
There a lot of long form idea maps/pdfs, diagrams, and videos.
I can convert and or integrate them into intuitive and interactive tutorial overlays of the web app or app to help users build the muscle memory of using Benzinga services
Visual overlays with highlighting arrows and background instructional audio and or Picture in Picture video to facilitate tutorials
I can create in depth execution plans, timelines, and simulated resource utilization maps(financial,HR,etc.) for my solutions that integrate existing or desired team members and capital resources
Website benzinga.com


Proposal
Allow users to connect their trading account information and history to a Benzinga dashboard that scans through its services for related alerts
Allow traders to connect a broker to trade within the app
Allow a heat map view of those positions sorted and colored by different parameters 
Sorted by equity size
Colored by:
Aggregate score/rank of Benzinga analysis 
Allow time travel for heatmap
Make a review dashboard of missed signals and alerts from Benzinga that could have made historical trades more profitable
