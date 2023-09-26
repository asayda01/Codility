function Solution(X: number, Y: number, D: number): number {

    if ( ( Y - X ) % D === 0 ) {
        return Math.floor ( ( Y - X ) / D )
    }

    else {
        return Math.floor( ( Y - X ) / D ) + 1
    };

};
