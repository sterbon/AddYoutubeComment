# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import urllib2, json
import time 

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCX6OQ3DkcsbYNE6H8uQQuVA&maxResults=10&order=date&type=video&key=AIzaSyAc_wg2XAiKpruMEnHPn9bdvKPN3tGul7c"

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    isPosted = True

    while isPosted: 
        response = urllib2.urlopen(url)
        data = json.load(urllib2.urlopen(url))['items'][0]['id']['videoId']
        if data != 'wMuYiLby3-s' :
            request = youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                "videoId": data,
                "topLevelComment": {
                "snippet": {
                    "textOriginal": "already here!"
                    }
                }
                }
            }
            )
            res = request.execute()
            print(res)
            isPosted = False

        else :
            time.sleep(1)
            isPosted = True
            print "Not yet!"
        
if __name__ == "__main__":
    main()