function solution(distance, rocks, n) {
  rocks.sort((a, b) => a - b);
  rocks = [0, ...rocks, distance];

  let start = 0;
  let end = distance;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let cnt = 0,
      now = 0;

    for (let i = 1; i < rocks.length; i++) {
      if (rocks[i] - now < mid) {
        cnt++;
      } else {
        now = rocks[i];
      }
    }

    if (cnt <= n) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return end;
}
