#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
import numpy
# @lc code=start
class priceToSell:
    def priceToSell(self, reqArea, area, price):
        idx_to_remove = []
    # Iterate area
        for idx in range(0, len(area)):
            ar_idx_res = [ar_idx for ar_idx, val in enumerate(area) if val == area[idx] and idx != ar_idx]
            price_res = [price[idx] for idx in ar_idx_res]
            
            # get mean & std for current area
            if price_res:
                p_mean = numpy.mean(price_res)
                p_std = numpy.std(price_res, axis=0)
            else:
                continue
            
            if abs(price[idx] - p_mean) > 3 * p_std:
                idx_to_remove.append(idx)
                
        if idx_to_remove:
            area_res = [val for idx, val in enumerate(area) if idx not in idx_to_remove]
            price_res = [val for idx, val in enumerate(price) if idx not in idx_to_remove]
        else:
            area_res = area
            price_res = price
            
        def area_in_between(area_res, reqArea):
            for idx in range(0, (len(area_res) - 1)):
                if area_res[idx] < reqArea < area_res[idx+1]:
                    return idx
                    
        def price_interpolation(area_res, price_res, reqArea):
            smaller_area = None
            larger_area = None
            
            for ar in area_res:
                if ar < reqArea and (smaller_area is None or ar > smaller_area):
                    smaller_area = ar
                if ar > reqArea and (larger_area is None or ar < larger_area):
                    larger_area = ar
                    
            smaller_idx = [i for i, a in enumerate(area_res) if a == smaller_area]
            larger_idx = [i for i, a in enumerate(area_res) if a == larger_area]
            
            smaller_p = numpy.mean([price_res[i] for i in smaller_idx])
            larger_p = numpy.mean([price_res[i] for i in larger_idx])
            
            return (smaller_p + (larger_p - smaller_p) * (reqArea - smaller_area) / (larger_area - smaller_area)) 
            
        def price_extrapolation(area_res, price_res, reqArea):
            areas = sorted(set(area_res), reverse=True)[:2]
            mean_prices = [numpy.mean([p for a, p in zip(area_res, price_res) if a == area_lar]) for area_lar in areas]
            
            return (mean_prices[1] + (mean_prices[1] - mean_prices[0]) * (reqArea - areas[1]) / (areas[1] - areas[0]))
                
        req_area_idx = [idx for idx, val in enumerate(area_res) if val == reqArea]
        area_idx = area_in_between(area_res, reqArea)
            
        if len(area_res) == 0:
            price_fin = 1000
        elif len(area_res) == 1:
            price_fin = price[0]
        elif req_area_idx:
            price_fin = numpy.mean([price_res[idx] for idx in req_area_idx])
        elif area_idx:
            price_fin = price_interpolation(area_res, price_res, reqArea)
        elif not area_idx:
            price_fin = price_extrapolation(area_res, price_res, reqArea)
            
        if price_fin < 1000:
            price_fin = 1000
        elif price_fin > 1000000:
            price_fin = 1000000
        else:
            price_fin = int(price_fin)
            
        return price_fin
        
if __name__ == "__main__":
    priceToSell = priceToSell()
    valuation = priceToSell.priceToSell(2500, [1200, 1200, 1200, 2000], [15000, 11000, 17000, 25000])
    print(valuation)
    