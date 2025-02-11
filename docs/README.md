# Drug-Price-Availability-Tracker
## Objective:
This project monitors the availability of medications and detects potential shortages in real time.
It operates on a predefined set of drugs, which can be customized in the settings.

First, the system checks the registered "Rotpunkt Apotheken" to determine if the selected medication is available.
If the drug is not in stock at these pharmacies, it then verifies whether the medication is currently experiencing a shortage. 

Utilizing web scraping, data processing, and visualization, this project provides valuable insights into medication
availability, ensuring better accessibility and informed decision-making.


**Key Features:**
- Scrapes medication availability from Swiss pharmacy websites
- Identifies shortages and availability
- Deployable in a Dockerized environment

## Data Sources
This project scrapes data from Swiss pharmacy websites:
- [Drugshortage.ch](#https://www.drugshortage.ch) - Real-time drug shortages database
- [Zur Rose Pharmacy](#https://www.zurrose.ch/de/aerzte/nota/weshalb) - Online pharmacy availability
- [swica](#https://medikamente.swica.ch/list/index/letter/A) - Online pharmacy availability
- [Rotpunkt Apotheken](#https://www.rotpunkt-apotheken.ch/shop) - Pharmacy chain with stock listings


## Future update
This project is intended to collect data over time to predict trends therefore more features are going to be implemented.
**Key Features:**
- Visualize stock levels and historical data
- Provides alerts when a medication becomes unavailable