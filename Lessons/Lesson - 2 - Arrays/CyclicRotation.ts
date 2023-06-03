function CyclicRotation(A: any[], K: number): number[] {

    if (A.length === 0 ) return [];

    for (let i = 0; i < K; i++) {

        A.unshift(A.pop());

    };

    return A;

};