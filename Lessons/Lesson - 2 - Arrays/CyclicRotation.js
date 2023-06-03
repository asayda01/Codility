function solution(A, K) {

    for (let i = 0; i<K ; i++) {

        A.unshift(A.pop());

    };

    return A;
    
};

/*
function solution(A, K) {

  function reverse(arr, start, end) {

    while (start < end) {

      [arr[start], arr[end]] = [arr[end], arr[start]];
      start++;
      end--;
      
    }
  }

  K %= A.length;

  reverse(A, 0, (A.length - 1));
  reverse(A, 0, (K - 1));
  reverse(A, K, (A.length - 1));

  return A;

};

*/

/*


function solution(A, K) {

  const len = A.length;
  A.push(...A.splice(0, (-K % len + len) % len));
  return A;
  
}

*/