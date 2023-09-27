class Solution {

    public int solution(int X, int Y, int D) {

    if ( ( Y - X ) % D == 0 ) {
        return ( Y - X ) / D ;
    } ;

    return ( Y - X ) / D + 1 ;

    } ;

} ;