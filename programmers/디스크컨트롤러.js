function solution(jobs) {
  const n = jobs.length;
  let total = 0;
  let time = 0;
  let j = 0;

  jobs.sort((a, b) => a[0] - b[0]);

  const pq = [];

  while (j < n || pq.length !== 0) {
    if (n > j && time >= jobs[j][0]) {
      pq.push(jobs[j++]);
      pq.sort((a, b) => b[1] - a[1]);
      continue;
    }

    if (pq.length !== 0) {
      const cur = pq.pop();
      time += cur[1];
      total += time - cur[0];
    } else {
      time = jobs[j][0];
    }
  }

  return Math.floor(total / n);
}
