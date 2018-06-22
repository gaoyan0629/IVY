import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener
consumer_key = 'ir4RvjLvoUDGrRW7cRIU2N3YN'
consumer_key_secret = 'DTpeoR4eFdjvN2vbS8Jz1KdTPTMbCGWQgsJ3V7rfKorBUR7u6G'
access_token = '2165990744-2IOgibizCnamq75Lh3okCuAYut6shKjoEeaicJi'
access_token_secret = 'k2BEfUoAKbdCRJp6wfqd7LYHinsU5L70hzMG2lflQ3YX7'

auth = OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)


class PrintListner(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source, '\n')

        def on_error(self, status_code):
            print("error code {}".format(status_code))
            return True

        def on_timeout(self):
            print("listner timeout")
            return True


def print_to_terminal():
    listner = PrintListner()
    stream = Stream(auth, listner)
    languages = ('en',)
    stream.sample(languages=languages)


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    print('Program started')
    # print_to_terminal()
    pull_down_tweets(auth.username)
