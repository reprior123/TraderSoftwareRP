 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 2</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_YEARS_UNCOVERED_COSTS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="years_uncovered_costs" value="nicht gedeckt, Kapitalverbrauch > 50,000 CHF" {if $data->years_uncovered_costs eq "nicht gedeckt, Kapitalverbrauch > 50,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_2_1_TEXT}<br>
    <input type="radio" name="years_uncovered_costs" value="nicht gedeckt, Kapitalverbrauch < 50,000 CHF" {if $data->years_uncovered_costs eq "nicht gedeckt, Kapitalverbrauch < 50,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_2_2_TEXT}<br>
    <input type="radio" name="years_uncovered_costs" value="gedeckt, weder Verbrauch noch Sparen" {if $data->years_uncovered_costs eq "gedeckt, weder Verbrauch noch Sparen"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_2_3_TEXT}<br>
    <input type="radio" name="years_uncovered_costs" value="gedeckt, Sparen < 50,000 CHF" {if $data->years_uncovered_costs eq "gedeckt, Sparen < 50,000 CHF"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_2_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="3" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
