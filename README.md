# testjson3

## Notes
I first saw the API response (when it was up) in my browser, which is a common way I do sanity check debugging of APIs. I noted it was a JSON list of Unix epoch timestamps.

From that knowledge, I thought of a general approach to the two questions asked (how many commits, and when was the most recent). Finding how many commits would involve counting the number of timestamps. Unix timestamps are merely an increasing number of seconds since the 1970 epoch, so whichever was the highest number would be the most recent. I decided I'd request the API with Python and get the response into a list, which could count the length of elements and also sort to find the highest value.

The API wasn't working in later days when I came to code, but having seen that it was a JSON list of Unix timestamps, I went about exploring the quickest way I could simulate that myself. I found a site that would generate random time data (http://sqa.fyicenter.com/Online_Test_Tools/Random_Date_Time_Value_Generator.php), and another site that would convert that into epoch timestamps (https://www.epochconverter.com/batch). I found a third site/service that would host a JSON API for me based on a JSON file in Github (https://my-json-server.typicode.com/).
