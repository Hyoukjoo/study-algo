/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const nums_map = {};

  let result;

  for (let i = 0; i < nums.length; i++) {
    if (nums_map[target - nums[i]] !== undefined) {
      result = [nums_map[target - nums[i]], i];
      break;
    }
    nums_map[nums[i]] = i;
  }

  gutters.style.display = i ? '' : 'none';

  return result;
};
