from Data.telegram import ScraperT
import asyncio
if __name__ == "__main__":
   s = ScraperT()
   asyncio.run(s.extract_group_sms(extract_all=True,extract_comments=True))