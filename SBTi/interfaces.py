from typing import Optional

from pydantic import BaseModel


class ScenarioInterface(BaseModel):
    number: int
    engagement_type: Optional[str]


class PortfolioCompany(BaseModel):
    company_name: str
    company_id: str
    investment_value: float
    engagement_target: Optional[str] = "False"


class DataProviderCompany(BaseModel):
    company_name: str
    company_id: str
    s1s2_emissions: float
    s3_emissions: float

    country: Optional[str]
    region: Optional[str]
    sector: Optional[str]
    industry_level_1: Optional[str]
    industry_level_2: Optional[str]
    industry_level_3: Optional[str]
    industry_level_4: Optional[str]

    company_revenue: Optional[float]
    company_market_cap: Optional[float]
    company_enterprise_value: Optional[float]
    company_total_assets: Optional[float]
    company_cash_equivalents: Optional[float]


class DataProviderTarget(BaseModel):
    company_id: str
    target_type: str
    intensity_metric: Optional[str]
    scope: str
    coverage_s1: float
    coverage_s2: float
    coverage_s3: float
    reduction_from_base_year: float
    base_year: int
    base_year_ghg_s1: float
    base_year_ghg_s2: float
    base_year_ghg_s3: float
    start_year: Optional[int]
    target_year: int
    reduction_from_base_year: float
    achieved_reduction: float