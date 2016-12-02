 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 1</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_YEARS_INCOME}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="years_income" value="< 100,000 CHF" {if $data->years_income eq "< 100,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_1_1_TEXT}<br>
    <input type="radio" name="years_income" value="100,001 - 200,000 CHF" {if $data->years_income eq "100,001 - 200,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_1_2_TEXT}<br>
    <input type="radio" name="years_income" value="201,000 - 500,000 CHF" {if $data->years_income eq "201,000 - 500,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_1_3_TEXT}<br>
    <input type="radio" name="years_income" value="501,000 - 1,000,000 CHF" {if $data->years_income eq "501,000 - 1,000,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_1_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="2" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
