 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 4</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_TOTAL_ASSETS_AMT}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="total_assets_amt" value="< 100,000 CHF" {if $data->total_assets_amt eq "< 100,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_4_1_TEXT}<br>
    <input type="radio" name="total_assets_amt" value="100,001 - 1,000,000 CHF" {if $data->total_assets_amt eq "100,001 - 1,000,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_4_2_TEXT}<br>
    <input type="radio" name="total_assets_amt" value="1,000,001 - 3,000,000 CHF" {if $data->total_assets_amt eq "1,000,001 - 3,000,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_4_3_TEXT}<br>
    <input type="radio" name="total_assets_amt" value="3,000,000 - 10,000,000 CHF" {if $data->total_assets_amt eq "3,000,000 - 10,000,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_4_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="5" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
