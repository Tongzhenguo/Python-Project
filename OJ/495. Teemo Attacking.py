# coding=utf-8
__author__ = 'arachis'
"""
In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition.
Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
在LLP世界，有一个名叫Teemo的英雄，他的攻击可以使他的敌人Ashe处于中毒状态。
现在，考虑到Teemo对阿什的攻击时间序列和Teemo进攻的中毒时间，您需要输出阿什处于中毒状态的总时间。
您可以假定Teemo在特定时间点的开始时发生攻击，并使Ashe立即处于中毒状态
Input: [1,2], 2
Output: 3
"""
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)#假设每次中毒时间都没有重叠
        for i in range(1,len(timeSeries)):#重叠时间是duration - (timeSeries[i] - timeSeries[i-1])
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans