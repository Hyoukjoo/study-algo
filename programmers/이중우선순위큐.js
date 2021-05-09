const operations = ['I 7', 'I 5', 'I -5', 'D -1'];

const arr = [];

for (let i = 0; i < operations.length; i++) {
  const op = operations[i].split(' ').map((v) => {
    if (isFinite(v)) {
      return Number(v);
    }
    return v;
  });

  if (op[0] === 'I') {
    arr.push(op[1]);
  } else {
    if (op[1] === '1') {
      arr.sort((a, b) => a - b);
      arr.pop();
    } else {
      arr.sort((a, b) => b - a);
      arr.pop();
    }
  }
}

console.log(arr);
