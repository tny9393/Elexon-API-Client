from datetime import date, time, datetime

METHODS = [
    {
        "data_type": "Transparency",
        "report_name": "B1720",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Amount Of Balancing Reserves Under Contract Service"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1730",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Prices Of Procured Balancing Reserves Service"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1740",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Accepted Aggregated Offers"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1750",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Activated Balancing Energy"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1760",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Prices Of Activated Balancing Energy"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1770",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Imbalance Prices"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1780",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Aggregated Imbalance Volumes"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1790",
        "parameters": [
            ('Year', int, []),
            ('Month', str, [])
        ],
        "Description": "Financial Expenses and Income For Balancing"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1810",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Cross-Border Balancing Volumes of Exchanged Bids and Offers"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1760",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Prices Of Activated Balancing Energy"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1820",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Cross-Border Balancing Prices"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1830",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Cross-border Balancing Energy Activated"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0610",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Actual Total Load per Bidding Zone"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0620",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Day-Ahead Total Load Forecast per Bidding Zone"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0630",
        "parameters": [
            ('Year', int, []),
            ('Week', int, [])
        ],
        "Description": "Week-Ahead Total Load Forecast per Bidding Zone"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0640",
        "parameters": [
            ('Year', int, []),
            ('Month', str, [])
        ],
        "Description": "Month-Ahead Total Load Forecast Per Bidding Zone"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0650",
        "parameters": [
            ('Year', int, [])
        ],
        "Description": "Year Ahead Total Load Forecast per Bidding Zone"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0810",
        "parameters": [
            ('Year', int, [])
        ],
        "Description": "Year Ahead Forecast Margin"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1410",
        "parameters": [
            ('Year', int, [])
        ],
        "Description": "Installed Generation Capacity Aggregated"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1430",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Day-Ahead Aggregated Generation"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1420",
        "parameters": [
            ('Year', int, [])
        ],
        "Description": "Installed Generation Capacity per Unit"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1440",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Generation forecasts for Wind and Solar"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1610",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, []),
            ('NGCBMUnitID', str, ['optional'])
        ],
        "Description": "Actual Generation Output per Generation Unit"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1630",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Actual Or Estimated Wind and Solar Power Generation"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1420",
        "parameters": [
            ('Year', int, [])
        ],
        "Description": "B0910"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1320",
        "parameters": [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        "Description": "Congestion Management Measures Countertrading"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1330",
        "parameters": [
            ('Year', int, []),
            ('Month', int, [])
        ],
        "Description": "Congestion Management Measures Costs of Congestion Management"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0710",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Planned Unavailability of Consumption Units"
    },
    {
        "data_type": "Transparency",
        "report_name": "B0720",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Changes In Actual Availability Of Consumption Units"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1010",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Planned Unavailability In The Transmission Grid"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1020",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Changes In Actual Availability In The Transmission Grid"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1030",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Changes In Actual Availability of Offshore Grid Infrastructure"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1510",
        "parameters":  [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Planned Unavailability of Generation Units"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1520",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Changes In Actual Availability of Generation Units"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1530",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Planned Unavailability of Production Units"
    },
    {
        "data_type": "Transparency",
        "report_name": "B1540",
        "parameters": [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        "Description": "Changes In Actual Availability of Production Units"
    },
    {
        "data_type": "REMIT",
        "report_name": "MessageListRetrieval",
        "parameters": [
            ('EventStart', date, ['optional']),
            ('EventEnd', date, ['optional']),
            ('PublicationFrom', date, ['optional']),
            ('PublicationTo', date, ['optional']),
            ('ParticipantId', str, ['optional']),
            ('MessageID', str, ['optional']),
            ('AssetID', str, ['optional']),
            ('EventType', str, ['optional']),
            ('FuelType', str, ['optional']),
            ('MessageType', str, ['optional']),
            ('UnavailabilityType', str, ['optional']),
            ('AffectedUnitID', str, ['optional']),
            ('ActiveFlag', str, ['optional'])
        ],
        "Description": "REMIT Flow - Message List Retrieval"
    },
    {
        "data_type": "Legacy",
        "report_name": "TEMP",
        "parameters": [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Temperature Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "BOD",
        "parameters":[
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        "Description": "Bid Offer Level Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "CDN",
        "parameters": [
            ('FromClearedDate', date, ['optional']),
            ('ToClearedDate', date, ['optional'])
        ],
        "Description": "Credit Default Notice Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "CDN",
        "parameters":  [
            ('FromClearedDate', date, ['optional']),
            ('ToClearedDate', date, ['optional'])
        ],
        "Description": "Credit Default Notice Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "SYSWARN",
        "parameters": [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "System Warnings"
    },
    {
        "data_type": "Legacy",
        "report_name": "DISBSAD",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        "Description": "Balancing Services Adjustment Action Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "NETBSAD",
        "parameters":  [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('IsTwoDayWindow', bool, ['optional'])
        ],
        "Description": "Balancing Service Adjustment Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "FREQ",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Rolling System Frequency"
    },
    {
        "data_type": "Legacy",
        "report_name": "MID",
        "parameters": [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional']),
            ('Period', str, ['optional'])
        ],
        "Description": "Market Index Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DEVINDOD",
        "parameters": [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Daily Energy Volume Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "QAS",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BmUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NgcBmUnitName', str, ['optional'])
        ],
        "Description": "Applicable Balancing Services Volume Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "ROLSYSDEM",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Rolling System Demand"
    },
    {
        "data_type": "Legacy",
        "report_name": "WINDFORPK",
        "parameters": [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Peak Wind Generation Forecast"
    },
    {
        "data_type": "Legacy",
        "report_name": "WINDFORFUELHH",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Wind Generation Forecast and Out-turn Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "FUELINSTHHCUR",
        "parameters": [
            ('FuelType', str, ['optional'])
        ],
        "Description": "Generation by Fuel Type (Current)"
    },
    {
        "data_type": "Legacy",
        "report_name": "FUELINST",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Generation by Fuel Type (Current)"
    },
    {
        "data_type": "Legacy",
        "report_name": "FUELHH",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Half Hourly Outturn Generation by Fuel Type"
    },
    {
        "data_type": "Legacy",
        "report_name": "INTERFUELHH",
        "parameters": [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        "Description": "Half Hourly Interconnector Outturn Generation"
    },
    {
        "data_type": "Legacy",
        "report_name": "NOU2T14D",
        "parameters": [],
        "Description": "National Output Useable (2-14 Days Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "FOU2T14D",
        "parameters": [],
        "Description": "National Output Useable by Fuel Type (2-14 Days Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "UOU2T14D",
        "parameters": [],
        "Description": "National Output Useable by Fuel Type and BM Unit (2-14 Days Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "NOU2T52W",
        "parameters": [],
        "Description": "National Output Useable (2-52 Weeks Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "FOU2T52W",
        "parameters": [],
        "Description": "National Output Useable by Fuel type (2-52 Weeks Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "UOU2T52W",
        "parameters": [],
        "Description": "National Output Useable by Fuel Type and BM Unit (2-52 Weeks Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "INDOITSDO",
        "parameters": [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Initial Demand Outturn"
    },
    {
        "data_type": "Legacy",
        "report_name": "MELIMBALNGC",
        "parameters": [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Forecast Day and Day Ahead Margin and Imbalance Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "FORDAYDEM",
        "parameters": [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        "Description": "Forecast Day and Day Ahead Demand Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DEMMF2T14D",
        "parameters": [],
        "Description": "Demand & Surplus Forecast Data (2-14 Days Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "DEMMF2T52W",
        "parameters": [],
        "Description": "Demand & Surplus Forecast Data (2-52 Weeks Ahead)"
    },
    {
        "data_type": "Legacy",
        "report_name": "SOSOP",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('StartTime', time, ['optional']),
            ('TradeType', str, ['optional']),
            ('IsTwoDayWindow', bool, ['optional'])
        ],
        "Description": "SO-SO Prices (SO-SO)"
    },
    {
        "data_type": "Legacy",
        "report_name": "PKDEMYESTTDYTOM",
        "parameters": [],
        "Description": "Peak Demand – Yesterday/Today/Tomorrow"
    },
    {
        "data_type": "Legacy",
        "report_name": "INDPKDEMINFO",
        "parameters": [],
        "Description": "Indicative Peak Demand Information (Using Operational Metering Data)"
    },
    {
        "data_type": "Legacy",
        "report_name": "INDTRIADDEMINFO",
        "parameters": [],
        "Description": "Indicative Triad Demand Information (Using Settlement Metering Data)"
    },
    {
        "data_type": "Legacy",
        "report_name": "PHYBMDATA",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        "Description": "Physical Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DYNBMDATA",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        "Description": "Dynamic Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DERBMDATA",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        "Description": "Derived BM Unit Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DERSYSDATA",
        "parameters": [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        "Description": "Derived System Wide Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "DETSYSPRICES",
        "parameters": [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        "Description": "Detailed System Prices"
    },
    {
        "data_type": "Legacy",
        "report_name": "MKTDEPTHDATA",
        "parameters": [
            ('SettlementDate', date, ['optional'])
        ],
        "Description": "Market Depth Data"
    },
    {
        "data_type": "Legacy",
        "report_name": "LATESTACCEPTS",
        "parameters": [],
        "Description": "Latest Acceptances"
    },
    {
        "data_type": "Legacy",
        "report_name": "HISTACCEPTS",
        "parameters":  [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        "Description": "Historic Acceptances"
    },
    {
        "data_type": "Legacy",
        "report_name": "SYSMSG",
        "parameters": [],
        "Description": "System Messages"
    },
    {
        "data_type": "Legacy",
        "report_name": "BMUNITSEARCH",
        "parameters":  [
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        "Description": "BM Unit Search"
    },
    {
        "data_type": "Legacy",
        "report_name": "SYSWARNTDYTOM",
        "parameters": [],
        "Description": "System Warning (Today/Tomorrow)"
    },
    {
        "data_type": "Legacy",
        "report_name": "HISTSYSWARN",
        "parameters": [],
        "Description": "System Warning (Historic)"
    },
    {
        "data_type": "Legacy",
        "report_name": "LOLPDRM",
        "parameters": [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional'])
        ],
        "Description": "Loss of Load Probability"
    },
    {
        "data_type": "Legacy",
        "report_name": "DEMCI",
        "parameters": [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional'])
        ],
        "Description": "Demand Control Instructions"
    },
    {
        "data_type": "Legacy",
        "report_name": "STORAW",
        "parameters": [
            ('FromSettlementDate', date, ['optional'])
        ],
        "Description": "STOR Availability Window"
    },
    {
        "data_type": "Legacy",
        "report_name": "TRADINGUNIT",
        "parameters": [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, []),
            ('TradeType', str, ['optional']),
            ('TradeName', str, ['optional'])
        ],
        "Description": "Trading Unit Delivery Mode"
    },
    {
        "data_type": "Legacy",
        "report_name": "EURGBFXDATA",
        "parameters":  [
            ('SettlementDayFrom', date, []),
            ('SettlementDayTo', date, ['optional'])
        ],
        "Description": "Settlement Exchange Rate"
    },
    {
        "data_type": "ReplacementReserveData",
        "report_name": "RRBidData",
        "parameters": [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('NGCBMUnitName', str, ['optional']),
            ('ParticipantId', str, ['optional'])
        ],
        "Description": "Replacement Reserve Data"
    },
    {
        "data_type": "ReplacementReserveData",
        "report_name": "RRAggregatedInfo",
        "parameters": [
            ('DateTimeFrom', datetime, []),
            ('DateTimeTo', datetime, ['optional'])
        ],
        "Description": " RR Aggregated Information Data"
    },
    {
        "data_type": "ReplacementReserveData",
        "report_name": "RRActivation",
        "parameters": [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional'])
        ],
        "Description": "RR Activation Data"
    },
    {
        "data_type": "ReplacementReserveData",
        "report_name": "RRINTCON",
        "parameters": [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('InterconnectorId', str, ['optional'])
        ],
        "Description": "RR Interconnector Schedule"
    },
    {
        "data_type": "ReplacementReserveData",
        "report_name": "RRGBNM",
        "parameters": [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional'])
        ],
        "Description": "RR GB Need Met"
    },
]