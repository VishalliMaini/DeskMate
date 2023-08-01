import os
import openai
from conf import apikey
openai.api_key =apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a invitation card of your marriage to your boss\n\nDear [Boss], \n\nWe cordially invite you to our wedding celebration! My fiancé [Name] and I are pleased to announce that we’re getting married on [Date] at [Time] and we would be delighted to have you there to share our special day. \n\nThe wedding will take place at [Venue] and will be followed by a reception at [Reception Venue]. \n\nWe would be so honored to have you attend our special day, and we hope that you will join us to celebrate. \n\nWith love, \n[Your Name] and [Fiancé’s Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
