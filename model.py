from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Uprtable(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    txt_ro_code = db.Column(db.String)
    txt_oo_code = db.Column(db.String)
    num_department_code = db.Column(db.db.BigInteger)
    num_product_code = db.Column(db.BigInteger) #	INT8,
    num_subproduct_cd = db.Column(db.BigInteger) # INT8,

    num_policy_year	= db.Column(db.BigInteger) #INT8,
    num_policy_term = db.Column(db.BigInteger)	#int8,
    txt_policy_no_char = db.Column(db.String)#varCHAR(20),
    num_reference_number = db.Column(db.BigInteger)#	INT8,
    num_endt_serial_no = db.Column(db.BigInteger)#	INT8,

    num_cancel_reference_number	= db.Column(db.BigInteger)#int8,
    txt_transaction_type_cd = db.Column(db.String)#	varCHAR(20),
    txt_proposal_status	= db.Column(db.String)#varCHAR(20),
    dat_policy_eff_from_date = db.Column(db.Date)#	date,	
    dat_endorsement_from_date = db.Column(db.Date)#	date,

    dat_accounting_date	= db.Column(db.Date)#DATE,
    dat_policy_end_date	= db.Column(db.Date)#date,	
    cur_premium_coll_incr = db.Column(db.BigInteger) #	DECIMAL(20,2),
    cur_premium_refu_incr = db.Column(db.BigInteger) #	DECIMAL(20,2),
    cur_terrorism_premium_coll = db.Column(db.BigInteger) #DECIMAL(20,2),

    cur_terrorism_premium_refu = db.Column(db.BigInteger) #DECIMAL(20,2),
    gdp_excl_terr_nucl		= db.Column(db.BigInteger) #DECIMAL(20,2),
    gdp_terrorism	= db.Column(db.BigInteger) #	DECIMAL(20,2),
    gdp_nuclear		= db.Column(db.BigInteger) #DECIMAL(20,2),
    gdp_incl_terr_nucl		= db.Column(db.BigInteger) #DECIMAL(20,2),

    prem_ref_period_end_date_365me= db.Column(db.Date)#	DATE	,
    prem_ref_period_start_date_365= db.Column(db.Date)#	DATE	,
    gross_direct_upr_excl_terr_nuc		= db.Column(db.BigInteger) #DECIMAL(20,2),
    upr_terr_365method		= db.Column(db.BigInteger) #DECIMAL(20,2),
    gross_direct_upr_nuclear_365me 	= db.Column(db.BigInteger) #DECIMAL(20,2))

    period_upr = db.Column(db.String)
    time_of_upload = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'txt_ro_code': self.txt_ro_code,
            'txt_oo_code': self.txt_oo_code,
            'num_department_code': self.num_department_code,
            'num_product_code': self.num_product_code,
            'num_subproduct_cd': self.num_subproduct_cd,

            'num_policy_year': self.num_policy_year,
            'num_policy_term': self.num_policy_term,
            'txt_policy_no_char': self.txt_policy_no_char,
            'num_reference_number': self.num_reference_number,
            'num_endt_serial_no': self.num_endt_serial_no,

            'num_cancel_reference_number': self.num_cancel_reference_number,
            'txt_transaction_type_cd': self.txt_transaction_type_cd,
            'txt_proposal_status': self.txt_proposal_status,
            'dat_policy_eff_from_date': self.dat_policy_eff_from_date,
            'dat_endorsement_from_date': self.dat_endorsement_from_date,

            'dat_accounting_date': self.dat_accounting_date,
            'dat_policy_end_date': self.dat_policy_end_date,
            'cur_premium_coll_incr': self.cur_premium_coll_incr,
            'cur_premium_refu_incr': self.cur_premium_refu_incr,
            'cur_terrorism_premium_coll': self.cur_terrorism_premium_coll,

            'cur_terrorism_premium_refu': self.cur_terrorism_premium_refu,
            'gdp_excl_terr_nucl': self.gdp_excl_terr_nucl,
            'gdp_terrorism': self.gdp_terrorism,
            'gdp_nuclear': self.gdp_nuclear,
            'gdp_incl_terr_nucl': self.gdp_incl_terr_nucl,

            'prem_ref_period_end_date_365me': self.prem_ref_period_end_date_365me,
            'prem_ref_period_start_date_365': self.prem_ref_period_start_date_365,
            'gross_direct_upr_excl_terr_nuc': self.gross_direct_upr_excl_terr_nuc,
            'upr_terr_365method': self.upr_terr_365method,
            'gross_direct_upr_nuclear_365me': self.gross_direct_upr_nuclear_365me,
        }
