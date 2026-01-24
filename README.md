# Environment-Telemetry-Backend
 A system that ingests environmental sensor data (CO2, temperature, energy usage), validates it, stores it reliably, and detects anomalies for emission spikes to support environmental analysis and reporting.

 ## Problems
 Environment data is often noisy, incomplete, or unreliable. Companies and researchers need a trustworthy system that validates incoming sensor data, store it safely, and detect anomalies such as emission spikes or sustain threshhold violations.

 ## Users
 - Environmental analysts
 - Researchers
 - Companies monitoring CO₂ emissions and environmental impact

 ## System Responsiblities
 - Ingest environmental sensor data via an API
 - Validates timestamps, sensor IDs, and measurement ranges
 - Store time-series data reliably
 - Detect emission anomalies and spikes
 - Provide query access for analysis and reporting

 ## Current Status
 Phase 1: Data ingestion and validation
