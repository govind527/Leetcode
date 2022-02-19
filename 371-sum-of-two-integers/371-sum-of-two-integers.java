/*Notes:add bit by bit, be mindful of carry, after adding, if carry is still 1, then add it as well;
*/
class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int temp=(a&b)<<1;
            a=a^b;
            b=temp;
        }
        return a;
        
    }
}