---
url: https://expo.dev/security
title: https://expo.dev/security
date: 2025-04-30T17:19:39.682141
depth: 2
---

# [Security & Compliance](https://expo.dev/security#security--compliance)
Last updated February 25th, 2025
Expo is committed to ensuring that Expo Application Services is continuously available and keeps your data secure. Expo uses a variety of industry-standard technologies and services to secure your data from unauthorized access, disclosure, use, and loss.
Security at Expo is directed by Expo's Chief Technology Officer and maintained by our Infrastructure team.
## [Infrastructure Security and Reliability](https://expo.dev/security#infrastructure-security-and-reliability)
### [Cloud platform security](https://expo.dev/security#cloud-platform-security)
Expo services are primarily hosted on Google Cloud Platform, providing best-in-class physical and logical security. Therefore, Expo services are built upon secure infrastructure as described in the [Google infrastructure security design overview](https://cloud.google.com/docs/security/infrastructure/design). You can also read further about the security polices and practices behind the operation of Google Cloud Platform in the [Google security overview](https://cloud.google.com/security/whitepaper) whitepaper.
### [Reliability](https://expo.dev/security#reliability)
Expo strives to maintain high operational availability of our services platform. You can see the current status and recent availability history at [status.expo.dev](https://status.expo.dev/).
## [Business Continuity and Disaster Recovery](https://expo.dev/security#business-continuity-and-disaster-recovery)
Expo's GCP infrastructure is properly configured as high-availability to ensure proper failover in case of a zone failure. Daily encrypted backups are kept in GCP. While never expected, we are prepared to restore data from backups in the event of a production data loss. Expo performs regular technical and procedural testing of our disaster recovery plan.
## [Data Security and Privacy](https://expo.dev/security#data-security-and-privacy)
### [End-user data](https://expo.dev/security#end-user-data)
Expo Application Services involves building and distributing your application code, not your application data. Thus, Expo is not aware of your users' identities and does not store or handle PII related to your users. If you use the Expo push notification service to distribute push notifications, Expo will store the push tokens required to send notifications to your users and will delete the push notification payload after it has been sent to Google FCM or Apple APNs. EAS Update uses randomly generated device install IDs to determine which devices have requested an update. You can read more about the data we collect and how we handle it in our [Privacy Explained document](https://expo.dev/privacy-explained).
In all scenarios regarding our users' data, Expo is GDPR-, CCPA-, and Data Privacy Framework-compliant.
### [Data encryption](https://expo.dev/security#data-encryption)
Data is encrypted in transit and at rest. Expo uses HTTPS to encrypt data in transit and encrypts data at rest using industry-standard encryption algorithms, including AES-256 or greater.
### [Data retention](https://expo.dev/security#data-retention)
EAS Build workers are ephemeral VMs, which are cleared after each use, and use a fresh image on each build, ensuring your application source code is not exposed to another account's build job. EAS Build logs and artifacts are stored for up to 90 days before being deleted. Backups are deleted 90 days or sooner after they are created.
### [Data removal](https://expo.dev/security#data-removal)
User data is immediately scheduled for timely deletion upon deletion of a user profile or account. To ensure they are authorized to do so, users must delete their accounts from within the Expo user interface. One a user profile or account is deleted, a job is initiated to delete any corresponding records stored by a [subprocessor](https://expo.dev/privacy/subprocessors).
## [Application Security](https://expo.dev/security#application-security)
### [Multi-factor authentication](https://expo.dev/security#multi-factor-authentication)
Individual user profiles can enable multi-factor authentication (MFA) to add an extra layer of security to their accounts. MFA requires users to provide two or more verification factors to access their accounts, such as a time-based one-time password (TOTP) or backup key, in addition to a password. Additional factors are also required when logging in via the Expo or EAS CLIs.
Note that Expo staff are unable to bypass the additional login factors to recover an account with MFA enabled where the MFA device or one-time codes has been lost.
### [Single-sign on](https://expo.dev/security#single-sign-on)
Organizations with Enterprise plans can enable single-sign on (SSO) to allow their users to log in to Expo using their existing identity provider. This allows organizations to manage their users' access to Expo using their existing identity management system. Supported identify providers include Okta, OneLogin, Google, and Microsoft Entra ID.
### [Audit logging](https://expo.dev/security#audit-logging)
Audit logs of administrative activities are available for Enterprise subscribers. These logs include information about users added and removed, API tokens generated, changes to build and deploy credentials, and other actions.
## [Security Policies](https://expo.dev/security#security-policies)
Expo maintains security polices, which are reviewed annually and updated regularly. These policies include:
  * Asset Management
  * Data Protection
  * Data Retention
  * Information Security
  * Incident Response
  * Risk Assessment
  * Software Development Life Cycle
  * System Access Control
  * Vendor Management
  * Vulnerability Management


Expo conducts background checks for all new personnel and requires annual security training.
## [Compliance](https://expo.dev/security#compliance)
Expo is SOC 2 Type 2-compliant. Our compliance attestation is for the Security trust services criterion. Enterprise customers can request a copy of the SOC 2 Type 2 report via our [compliance report request page](https://app.drata.com/trust/9cc346b0-0c38-11ee-865f-029d78a187d9).
## [Vulnerability Disclosure](https://expo.dev/security#vulnerability-disclosure)
Vulnerabilities and security concerns related to Expo tools can be reported to security-reports@expo.dev. Be sure to include a proof of concept, a list of tools used (including versions), and the output of the tools. We take all disclosures seriously and will respond to valid reports as we verify the vulnerability and develop a fix.
Be aware that our bug bounties are typically reserved for confirmed reports of vulnerabilities that are comparable in severity to RCE.

