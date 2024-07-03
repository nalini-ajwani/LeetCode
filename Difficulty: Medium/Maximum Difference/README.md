<h2><a href="https://www.geeksforgeeks.org/problems/maximum-difference-1587115620/1?page=2&category=Stack&sortBy=submissions">Maximum Difference</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an integer array <strong>arr</strong> of length <strong>n</strong>, the task is to find the maximum absolute difference between the <strong>nearest left smaller</strong> and <strong>nearest right</strong> <strong>smaller element</strong> of every element in array arr. If for any element in the arr, the nearest smaller element doesn't exist then consider it as 0.</span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong><br>n = 3<br>arr = {2, 1, 8}
<strong>Output:</strong> 1
left smaller  ls = {0, 0, 1}
right smaller rs = {1, 0, 0}
Maximum Diff of abs(ls[i] - rs[i]) = <strong>1</strong></span></pre>
<p><span style="font-size: 18px;"><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-size: medium; white-space: normal;"><span style="font-size: 18px;">Example 2:</span></strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong><br>n = 7<br>arr = {2, 4, 8, 7, 7, 9, 3}
<strong>Output:</strong> 4
left smaller   ls = {0, 2, 4, 4, 4, 7, 2}
right smaller  rs = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(ls[i] - rs[i]) = abs(7 - 3) = <strong>4</strong></span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:<br></strong>You have to complete the function <strong>findMaxDiff( )</strong>, which takes a vector <strong>arr</strong> as input parameter and integer n, the length of vector arr is n, and returns the maximum difference according to the problem description.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(n)<br><strong>Expected Auxilary Space:</strong> O(n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 10<sup>6</sup><br>1&lt;= arr[i] &lt;=10<sup>9</sup><br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Stack</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;