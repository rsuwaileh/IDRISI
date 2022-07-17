import json
import argparse

def load_input_tweets(input_path):
    tweets = {}
    for line in open(input_path, encoding='utf-8').read().splitlines(): 
        tweet = json.loads(line)
        tweets[tweet["tweet_id"]] = tweet["text"]
    return tweets
    
def check_format(out_path, tweets):
    i = 0
    errors = 0

    for line in open(out_path, encoding='utf-8').read().splitlines(): 
        try:
            tweet = json.loads(line)
        except:  # includes JSONDecodeError                          
            print("line {} is not in JSON format".format(i+1))
            errors +=1

        if "tweet_id" not in tweet:
            print("line {} has no attribute \"tweet_id\"".format(i+1))
            errors +=1
        else:
            it = tweet["tweet_id"]

        if "location_mentions" not in tweet:
            print("line {} has no attribute \"location_mentions\"".format(i+1))
            errors +=1
        else:
            j = 0
            for loc in tweet["location_mentions"]:
                if "text" not in loc:
                    print("LM {} in line {} has no attribute \"text\"".format(j+1, i+1))
                else:
                    tloc = loc["text"]
                    if "start_offset" not in loc:
                        print("LM {} in line {} has no attribute \"start_offset\"".format(j+1, i+1))
                    else:
                        sloc = loc["start_offset"] 
                        if "end_offset" not in loc:
                            print("LM {} in line {} has no attribute \"end_offset\"".format(j+1, i+1))
                        else:
                            eloc = loc["end_offset"]

                            if tweets[it] and tweets[it][sloc:eloc] != tloc:
                                print("LM \"{}\" doesn't exist in tweets {}, check the loc offsets".format(tloc, it) )

                    j += 1

        i += 1

    if errors > 0:
        print("The output file has issues! Please fix issues above and run the checker again!")
    else:
        print("The output file had passed all checks successfully!")


def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
            "--input_path",
            default=None,
            type=str,
            required=True,
            help="The path to the file that contains the input path in JSONL format",
    )

    parser.add_argument(
            "--output_path",
            default=None,
            type=str,
            required=True,
            help="The path to the file that contains the output of the system in JSONL format",
    )
    
    args = parser.parse_args()


    tweets = load_input_tweets(args.input_path)
    check_format(args.output_path, tweets)
    
if __name__ == "__main__":
        main()


