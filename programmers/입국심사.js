function solution(n, times) {
  times.sort((a, b) => a - b);
  let left = 1;
  let right = n * times[times.length - 1];
  let mid = Math.floor((left + right) / 2);

  while (left <= right) {
    let count = times.reduce((acc, cur) => acc + Math.floor(mid / cur), 0);
    if (count >= n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
    mid = Math.floor((left + right) / 2);
  }

  return left;
}
