### Order Types.
Possible Values	Description
1	Limit order
2	Market order
3	Stop order (SL-M)
4	Stoplimit order (SL-L)

## Request attributes

Attribute	Data Type	Description
symbol*	string	Eg: NSE:SBIN-EQ
qty*	int	The quantity should be in multiples of lot size for derivatives.
type*	int	
1 => Limit Order
2 => Market Order
3 => Stop Order (SL-M)
4 => Stoplimit Order (SL-L)
View Details
side*	int	
1 => Buy
-1 => Sell
View Details
productType*	string	
CNC => For equity only
INTRADAY => Applicable for all segments.
MARGIN => Applicable only for derivatives
CO => Cover Order
BO => Bracket Order
MTF => Approved Symbols Only
View Details
limitPrice*	float	Default => 0
Provide valid price for Limit and Stoplimit orders
stopPrice*	float	Default => 0
Provide valid price for Stop and Stoplimit orders
disclosedQty*	int	Default => 0
Allowed only for Equity
validity*	string	IOC => Immediate or Cancel
DAY => Valid till the end of the day
offlineOrder*	boolean	False => When market is open
True => When placing AMO order
stopLoss*	float	Default => 0
Provide valid price for CO and BO orders
takeProfit*	float	Default => 0
Provide valid price for BO orders
orderTag	string	(Optional) Tag you want to assign to the specific order
isSliceOrder	boolean	False => The full quantity is placed as one single order.
True => The quantity is placed in multiple smaller orders if the total quantity is more than the freeze quantity.
