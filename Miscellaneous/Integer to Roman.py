class Solution:
    def intToRoman(self, num: int) -> str:
        dict_roman = [['I','V'],['X','L'],['C','D'],['M','']]
        ans=''
        i=0
        while(num>0 and i<3):
            digit = num%10
            if(digit<4):
                ans = dict_roman[i][0]*digit+ans
            elif(digit<9):
                ans = dict_roman[i][0]*(5-digit)+dict_roman[i][1]+dict_roman[i][0]*(digit-5)+ans
            else:ans = dict_roman[i][0]+dict_roman[i+1][0]+ans
            num//=10
            i+=1
        return ans if num<=0 else dict_roman[3][0]*num+ans
        
