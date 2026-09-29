"""Contains all the data models used in inputs/outputs"""

from .advisory_details import AdvisoryDetails
from .advisory_head import AdvisoryHead
from .advisory_summary import AdvisorySummary
from .advisory_vulnerability_head import AdvisoryVulnerabilityHead
from .analysis_advisory import AnalysisAdvisory
from .analysis_details import AnalysisDetails
from .analysis_details_status import AnalysisDetailsStatus
from .analysis_details_v3 import AnalysisDetailsV3
from .analysis_purl_status import AnalysisPurlStatus
from .analysis_request import AnalysisRequest
from .analysis_response import AnalysisResponse
from .analysis_response_v3 import AnalysisResponseV3
from .analysis_result import AnalysisResult
from .analysis_result_v3 import AnalysisResultV3
from .analysis_status import AnalysisStatus
from .analysis_status_details import AnalysisStatusDetails
from .analyze_request import AnalyzeRequest
from .analyze_response import AnalyzeResponse
from .auth_config import AuthConfig
from .auth_method_type_0 import AuthMethodType0
from .auth_method_type_0_type import AuthMethodType0Type
from .auth_method_type_1 import AuthMethodType1
from .auth_method_type_1_type import AuthMethodType1Type
from .auth_method_type_2 import AuthMethodType2
from .auth_method_type_2_type import AuthMethodType2Type
from .base_purl_details import BasePurlDetails
from .base_purl_head import BasePurlHead
from .base_score import BaseScore
from .base_summary import BaseSummary
from .bulk_assignment_request import BulkAssignmentRequest
from .cache_status_details import CacheStatusDetails
from .cache_status_entry import CacheStatusEntry
from .clearly_defined_curation_importer import ClearlyDefinedCurationImporter
from .clearly_defined_importer import ClearlyDefinedImporter
from .clearly_defined_package_type import ClearlyDefinedPackageType
from .common_importer import CommonImporter
from .component_result import ComponentResult
from .create_response import CreateResponse
from .credential_source_type_0 import CredentialSourceType0
from .credential_source_type_0_type import CredentialSourceType0Type
from .credential_source_type_1 import CredentialSourceType1
from .credential_source_type_1_type import CredentialSourceType1Type
from .credential_source_type_2 import CredentialSourceType2
from .credential_source_type_2_type import CredentialSourceType2Type
from .csaf_importer import CsafImporter
from .cve_importer import CveImporter
from .cwe_importer import CweImporter
from .error_information import ErrorInformation
from .exploit import Exploit
from .exploit_intelligence_finding import ExploitIntelligenceFinding
from .exploit_intelligence_job_details import ExploitIntelligenceJobDetails
from .exploit_intelligence_job_status import ExploitIntelligenceJobStatus
from .exploit_intelligence_job_summary import ExploitIntelligenceJobSummary
from .exploit_metadata import ExploitMetadata
from .external_reference_query import ExternalReferenceQuery
from .extract_package import ExtractPackage
from .extract_result import ExtractResult
from .extract_result_packages import ExtractResultPackages
from .format_ import Format
from .get_purl_deprecated import GetPurlDeprecated
from .group import Group
from .group_list_result import GroupListResult
from .group_request import GroupRequest
from .http_discovery_type_0 import HttpDiscoveryType0
from .http_discovery_type_0_type import HttpDiscoveryType0Type
from .http_importer import HttpImporter
from .importer import Importer
from .importer_configuration_type_0 import ImporterConfigurationType0
from .importer_configuration_type_1 import ImporterConfigurationType1
from .importer_configuration_type_2 import ImporterConfigurationType2
from .importer_configuration_type_3 import ImporterConfigurationType3
from .importer_configuration_type_4 import ImporterConfigurationType4
from .importer_configuration_type_5 import ImporterConfigurationType5
from .importer_configuration_type_6 import ImporterConfigurationType6
from .importer_configuration_type_7 import ImporterConfigurationType7
from .importer_configuration_type_8 import ImporterConfigurationType8
from .importer_configuration_type_9 import ImporterConfigurationType9
from .importer_configuration_type_10 import ImporterConfigurationType10
from .importer_data import ImporterData
from .importer_report import ImporterReport
from .info_response_200 import InfoResponse200
from .info_response_200_build import InfoResponse200Build
from .ingest_result import IngestResult
from .kev_importer import KevImporter
from .labels import Labels
from .license_category import LicenseCategory
from .license_info import LicenseInfo
from .license_ref_mapping import LicenseRefMapping
from .license_summary import LicenseSummary
from .license_text import LicenseText
from .list_advisories_deprecated import ListAdvisoriesDeprecated
from .list_related_packages_which import ListRelatedPackagesWhich
from .list_sbom_groups_parents import ListSbomGroupsParents
from .message import Message
from .node import Node
from .nvd_importer import NvdImporter
from .organization_details import OrganizationDetails
from .organization_head import OrganizationHead
from .osv_importer import OsvImporter
from .paginated_results_advisory_summary import PaginatedResultsAdvisorySummary
from .paginated_results_advisory_summary_items_item import (
    PaginatedResultsAdvisorySummaryItemsItem,
)
from .paginated_results_base_purl_summary import PaginatedResultsBasePurlSummary
from .paginated_results_exploit import PaginatedResultsExploit
from .paginated_results_exploit_intelligence_job_summary import (
    PaginatedResultsExploitIntelligenceJobSummary,
)
from .paginated_results_exploit_intelligence_job_summary_items_item import (
    PaginatedResultsExploitIntelligenceJobSummaryItemsItem,
)
from .paginated_results_exploit_items_item import PaginatedResultsExploitItemsItem
from .paginated_results_exploit_items_item_metadata import (
    PaginatedResultsExploitItemsItemMetadata,
)
from .paginated_results_group_details import PaginatedResultsGroupDetails
from .paginated_results_group_details_items_item import (
    PaginatedResultsGroupDetailsItemsItem,
)
from .paginated_results_importer_report import PaginatedResultsImporterReport
from .paginated_results_importer_report_items_item import (
    PaginatedResultsImporterReportItemsItem,
)
from .paginated_results_license_summary import PaginatedResultsLicenseSummary
from .paginated_results_license_summary_items_item import (
    PaginatedResultsLicenseSummaryItemsItem,
)
from .paginated_results_license_text import PaginatedResultsLicenseText
from .paginated_results_license_text_items_item import (
    PaginatedResultsLicenseTextItemsItem,
)
from .paginated_results_node import PaginatedResultsNode
from .paginated_results_node_items_item import PaginatedResultsNodeItemsItem
from .paginated_results_organization_summary import PaginatedResultsOrganizationSummary
from .paginated_results_product_summary import PaginatedResultsProductSummary
from .paginated_results_product_summary_items_item import (
    PaginatedResultsProductSummaryItemsItem,
)
from .paginated_results_purl_summary import PaginatedResultsPurlSummary
from .paginated_results_purl_summary_items_item import (
    PaginatedResultsPurlSummaryItemsItem,
)
from .paginated_results_purl_summary_items_item_qualifiers import (
    PaginatedResultsPurlSummaryItemsItemQualifiers,
)
from .paginated_results_sbom_model import PaginatedResultsSbomModel
from .paginated_results_sbom_model_items_item import PaginatedResultsSbomModelItemsItem
from .paginated_results_sbom_model_items_item_properties import (
    PaginatedResultsSbomModelItemsItemProperties,
)
from .paginated_results_sbom_package import PaginatedResultsSbomPackage
from .paginated_results_sbom_package_items_item import (
    PaginatedResultsSbomPackageItemsItem,
)
from .paginated_results_sbom_package_relation_sbom_package import (
    PaginatedResultsSbomPackageRelationSbomPackage,
)
from .paginated_results_sbom_package_relation_sbom_package_items_item import (
    PaginatedResultsSbomPackageRelationSbomPackageItemsItem,
)
from .paginated_results_sbom_package_relation_sbom_package_items_item_package import (
    PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage,
)
from .paginated_results_sbom_summary import PaginatedResultsSbomSummary
from .paginated_results_sbom_summary_items_item import (
    PaginatedResultsSbomSummaryItemsItem,
)
from .paginated_results_sbom_summary_sbom_package import (
    PaginatedResultsSbomSummarySbomPackage,
)
from .paginated_results_sbom_summary_sbom_package_items_item import (
    PaginatedResultsSbomSummarySbomPackageItemsItem,
)
from .paginated_results_sbom_summary_sbom_package_items_item_described_by_item import (
    PaginatedResultsSbomSummarySbomPackageItemsItemDescribedByItem,
)
from .paginated_results_sbom_summary_sbom_package_summary import (
    PaginatedResultsSbomSummarySbomPackageSummary,
)
from .paginated_results_sbom_summary_sbom_package_summary_items_item import (
    PaginatedResultsSbomSummarySbomPackageSummaryItemsItem,
)
from .paginated_results_sbom_summary_sbom_package_summary_items_item_described_by_item import (
    PaginatedResultsSbomSummarySbomPackageSummaryItemsItemDescribedByItem,
)
from .paginated_results_spdx_license_summary import PaginatedResultsSpdxLicenseSummary
from .paginated_results_spdx_license_summary_items_item import (
    PaginatedResultsSpdxLicenseSummaryItemsItem,
)
from .paginated_results_vulnerability_summary import (
    PaginatedResultsVulnerabilitySummary,
)
from .paginated_results_weakness_summary import PaginatedResultsWeaknessSummary
from .patch_assignment_request import PatchAssignmentRequest
from .product_details import ProductDetails
from .product_head import ProductHead
from .product_sbom_head import ProductSbomHead
from .product_summary import ProductSummary
from .product_version_details import ProductVersionDetails
from .product_version_head import ProductVersionHead
from .progress import Progress
from .progress_details import ProgressDetails
from .purl_advisory import PurlAdvisory
from .purl_details import PurlDetails
from .purl_head import PurlHead
from .purl_status import PurlStatus
from .purl_summary import PurlSummary
from .purl_summary_qualifiers import PurlSummaryQualifiers
from .quay_importer import QuayImporter
from .recommend_entry import RecommendEntry
from .recommend_report_impact_summary import RecommendReportImpactSummary
from .recommend_report_package import RecommendReportPackage
from .recommend_report_request import RecommendReportRequest
from .recommend_report_response import RecommendReportResponse
from .recommend_report_sbom import RecommendReportSbom
from .recommend_request import RecommendRequest
from .recommend_response import RecommendResponse
from .recommend_response_recommendations import RecommendResponseRecommendations
from .relationship import Relationship
from .remediation_category import RemediationCategory
from .remediation_summary import RemediationSummary
from .render_sbom_graph_ext import RenderSbomGraphExt
from .report import Report
from .report_messages import ReportMessages
from .report_messages_additional_property import ReportMessagesAdditionalProperty
from .requested_field_hash_map_hash_map_type_0 import RequestedFieldHashMapHashMapType0
from .revisioned_importer import RevisionedImporter
from .revisioned_importer_value import RevisionedImporterValue
from .sbom_advisory import SbomAdvisory
from .sbom_head import SbomHead
from .sbom_importer import SbomImporter
from .sbom_model import SbomModel
from .sbom_model_properties import SbomModelProperties
from .sbom_package import SbomPackage
from .sbom_package_summary import SbomPackageSummary
from .sbom_status import SbomStatus
from .sbom_summary import SbomSummary
from .score import Score
from .score_type import ScoreType
from .scored_vector import ScoredVector
from .severity import Severity
from .source_document import SourceDocument
from .spdx_license_details import SpdxLicenseDetails
from .spdx_license_summary import SpdxLicenseSummary
from .state import State
from .status_context_type_0 import StatusContextType0
from .status_context_type_1 import StatusContextType1
from .update import Update
from .upload_advisory_format import UploadAdvisoryFormat
from .upload_sbom_cache import UploadSbomCache
from .upload_sbom_format import UploadSbomFormat
from .version_range_type_1 import VersionRangeType1
from .versioned_purl_head import VersionedPurlHead
from .versioned_purl_summary import VersionedPurlSummary
from .vex_justification_type_0 import VexJustificationType0
from .vex_justification_type_1 import VexJustificationType1
from .vex_justification_type_2 import VexJustificationType2
from .vex_justification_type_3 import VexJustificationType3
from .vex_justification_type_4 import VexJustificationType4
from .vex_justification_type_5 import VexJustificationType5
from .vex_justification_type_6 import VexJustificationType6
from .vex_status_type_0 import VexStatusType0
from .vex_status_type_1 import VexStatusType1
from .vex_status_type_2 import VexStatusType2
from .vex_status_type_3 import VexStatusType3
from .vex_status_type_4 import VexStatusType4
from .vex_status_type_5 import VexStatusType5
from .vulnerability_advisory_head import VulnerabilityAdvisoryHead
from .vulnerability_advisory_status import VulnerabilityAdvisoryStatus
from .vulnerability_advisory_summary import VulnerabilityAdvisorySummary
from .vulnerability_advisory_summary_purls import VulnerabilityAdvisorySummaryPurls
from .vulnerability_details import VulnerabilityDetails
from .vulnerability_head import VulnerabilityHead
from .vulnerability_sbom_status import VulnerabilitySbomStatus
from .vulnerability_sbom_status_purl_statuses import VulnerabilitySbomStatusPurlStatuses
from .vulnerability_status import VulnerabilityStatus
from .weakness_details import WeaknessDetails
from .weakness_head import WeaknessHead

__all__ = (
    "AdvisoryDetails",
    "AdvisoryHead",
    "AdvisorySummary",
    "AdvisoryVulnerabilityHead",
    "AnalysisAdvisory",
    "AnalysisDetails",
    "AnalysisDetailsStatus",
    "AnalysisDetailsV3",
    "AnalysisPurlStatus",
    "AnalysisRequest",
    "AnalysisResponse",
    "AnalysisResponseV3",
    "AnalysisResult",
    "AnalysisResultV3",
    "AnalysisStatus",
    "AnalysisStatusDetails",
    "AnalyzeRequest",
    "AnalyzeResponse",
    "AuthConfig",
    "AuthMethodType0",
    "AuthMethodType0Type",
    "AuthMethodType1",
    "AuthMethodType1Type",
    "AuthMethodType2",
    "AuthMethodType2Type",
    "BasePurlDetails",
    "BasePurlHead",
    "BaseScore",
    "BaseSummary",
    "BulkAssignmentRequest",
    "CacheStatusDetails",
    "CacheStatusEntry",
    "ClearlyDefinedCurationImporter",
    "ClearlyDefinedImporter",
    "ClearlyDefinedPackageType",
    "CommonImporter",
    "ComponentResult",
    "CreateResponse",
    "CredentialSourceType0",
    "CredentialSourceType0Type",
    "CredentialSourceType1",
    "CredentialSourceType1Type",
    "CredentialSourceType2",
    "CredentialSourceType2Type",
    "CsafImporter",
    "CveImporter",
    "CweImporter",
    "ErrorInformation",
    "Exploit",
    "ExploitIntelligenceFinding",
    "ExploitIntelligenceJobDetails",
    "ExploitIntelligenceJobStatus",
    "ExploitIntelligenceJobSummary",
    "ExploitMetadata",
    "ExternalReferenceQuery",
    "ExtractPackage",
    "ExtractResult",
    "ExtractResultPackages",
    "Format",
    "GetPurlDeprecated",
    "Group",
    "GroupListResult",
    "GroupRequest",
    "HttpDiscoveryType0",
    "HttpDiscoveryType0Type",
    "HttpImporter",
    "Importer",
    "ImporterConfigurationType0",
    "ImporterConfigurationType1",
    "ImporterConfigurationType2",
    "ImporterConfigurationType3",
    "ImporterConfigurationType4",
    "ImporterConfigurationType5",
    "ImporterConfigurationType6",
    "ImporterConfigurationType7",
    "ImporterConfigurationType8",
    "ImporterConfigurationType9",
    "ImporterConfigurationType10",
    "ImporterData",
    "ImporterReport",
    "InfoResponse200",
    "InfoResponse200Build",
    "IngestResult",
    "KevImporter",
    "Labels",
    "LicenseCategory",
    "LicenseInfo",
    "LicenseRefMapping",
    "LicenseSummary",
    "LicenseText",
    "ListAdvisoriesDeprecated",
    "ListRelatedPackagesWhich",
    "ListSbomGroupsParents",
    "Message",
    "Node",
    "NvdImporter",
    "OrganizationDetails",
    "OrganizationHead",
    "OsvImporter",
    "PaginatedResultsAdvisorySummary",
    "PaginatedResultsAdvisorySummaryItemsItem",
    "PaginatedResultsBasePurlSummary",
    "PaginatedResultsExploit",
    "PaginatedResultsExploitIntelligenceJobSummary",
    "PaginatedResultsExploitIntelligenceJobSummaryItemsItem",
    "PaginatedResultsExploitItemsItem",
    "PaginatedResultsExploitItemsItemMetadata",
    "PaginatedResultsGroupDetails",
    "PaginatedResultsGroupDetailsItemsItem",
    "PaginatedResultsImporterReport",
    "PaginatedResultsImporterReportItemsItem",
    "PaginatedResultsLicenseSummary",
    "PaginatedResultsLicenseSummaryItemsItem",
    "PaginatedResultsLicenseText",
    "PaginatedResultsLicenseTextItemsItem",
    "PaginatedResultsNode",
    "PaginatedResultsNodeItemsItem",
    "PaginatedResultsOrganizationSummary",
    "PaginatedResultsProductSummary",
    "PaginatedResultsProductSummaryItemsItem",
    "PaginatedResultsPurlSummary",
    "PaginatedResultsPurlSummaryItemsItem",
    "PaginatedResultsPurlSummaryItemsItemQualifiers",
    "PaginatedResultsSbomModel",
    "PaginatedResultsSbomModelItemsItem",
    "PaginatedResultsSbomModelItemsItemProperties",
    "PaginatedResultsSbomPackage",
    "PaginatedResultsSbomPackageItemsItem",
    "PaginatedResultsSbomPackageRelationSbomPackage",
    "PaginatedResultsSbomPackageRelationSbomPackageItemsItem",
    "PaginatedResultsSbomPackageRelationSbomPackageItemsItemPackage",
    "PaginatedResultsSbomSummary",
    "PaginatedResultsSbomSummaryItemsItem",
    "PaginatedResultsSbomSummarySbomPackage",
    "PaginatedResultsSbomSummarySbomPackageItemsItem",
    "PaginatedResultsSbomSummarySbomPackageItemsItemDescribedByItem",
    "PaginatedResultsSbomSummarySbomPackageSummary",
    "PaginatedResultsSbomSummarySbomPackageSummaryItemsItem",
    "PaginatedResultsSbomSummarySbomPackageSummaryItemsItemDescribedByItem",
    "PaginatedResultsSpdxLicenseSummary",
    "PaginatedResultsSpdxLicenseSummaryItemsItem",
    "PaginatedResultsVulnerabilitySummary",
    "PaginatedResultsWeaknessSummary",
    "PatchAssignmentRequest",
    "ProductDetails",
    "ProductHead",
    "ProductSbomHead",
    "ProductSummary",
    "ProductVersionDetails",
    "ProductVersionHead",
    "Progress",
    "ProgressDetails",
    "PurlAdvisory",
    "PurlDetails",
    "PurlHead",
    "PurlStatus",
    "PurlSummary",
    "PurlSummaryQualifiers",
    "QuayImporter",
    "RecommendEntry",
    "RecommendReportImpactSummary",
    "RecommendReportPackage",
    "RecommendReportRequest",
    "RecommendReportResponse",
    "RecommendReportSbom",
    "RecommendRequest",
    "RecommendResponse",
    "RecommendResponseRecommendations",
    "Relationship",
    "RemediationCategory",
    "RemediationSummary",
    "RenderSbomGraphExt",
    "Report",
    "ReportMessages",
    "ReportMessagesAdditionalProperty",
    "RequestedFieldHashMapHashMapType0",
    "RevisionedImporter",
    "RevisionedImporterValue",
    "SbomAdvisory",
    "SbomHead",
    "SbomImporter",
    "SbomModel",
    "SbomModelProperties",
    "SbomPackage",
    "SbomPackageSummary",
    "SbomStatus",
    "SbomSummary",
    "Score",
    "ScoreType",
    "ScoredVector",
    "Severity",
    "SourceDocument",
    "SpdxLicenseDetails",
    "SpdxLicenseSummary",
    "State",
    "StatusContextType0",
    "StatusContextType1",
    "Update",
    "UploadAdvisoryFormat",
    "UploadSbomCache",
    "UploadSbomFormat",
    "VersionRangeType1",
    "VersionedPurlHead",
    "VersionedPurlSummary",
    "VexJustificationType0",
    "VexJustificationType1",
    "VexJustificationType2",
    "VexJustificationType3",
    "VexJustificationType4",
    "VexJustificationType5",
    "VexJustificationType6",
    "VexStatusType0",
    "VexStatusType1",
    "VexStatusType2",
    "VexStatusType3",
    "VexStatusType4",
    "VexStatusType5",
    "VulnerabilityAdvisoryHead",
    "VulnerabilityAdvisoryStatus",
    "VulnerabilityAdvisorySummary",
    "VulnerabilityAdvisorySummaryPurls",
    "VulnerabilityDetails",
    "VulnerabilityHead",
    "VulnerabilitySbomStatus",
    "VulnerabilitySbomStatusPurlStatuses",
    "VulnerabilityStatus",
    "WeaknessDetails",
    "WeaknessHead",
)
