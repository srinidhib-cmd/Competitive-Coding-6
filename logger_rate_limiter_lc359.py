#Author: Srinidhi
#Did it run on LC: Yes
#Time Complexity: O(1) - Doing on key lookup at each call
#Space Complexity: O(n) - Where n is he number of unique messages encountered at that point
#Logic:
"""
Using a hashmap store in the form: message->timestamp
If message not seen, make an entry in the hashmap
If message is seen, 2 cases arise -> seen within 10 seconds,return False
else, return True
"""
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message not in self.message_hashmap.keys():
            self.message_hashmap[message] = timestamp
            return True
        else:
            time = self.message_hashmap[message]
            
            if abs(timestamp-time) >= 10:
                self.message_hashmap[message] = timestamp
                return True
            else:
                return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)