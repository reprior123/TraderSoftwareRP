 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 8</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_PRIMARY_FINANCIAL_GOAL}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="primary_financial_goal" value="Kapitalerhalt" {if $data->primary_financial_goal eq "Kapitalerhalt"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_8_1_TEXT}<br>
    <input type="radio" name="primary_financial_goal" value="Ausgewogenes Wachstum" {if $data->primary_financial_goal eq "Ausgewogenes Wachstum"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_8_2_TEXT}<br>
    <input type="radio" name="primary_financial_goal" value="Dynamisches Wachstum" {if $data->primary_financial_goal eq "Dynamisches Wachstum"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_8_3_TEXT}<br>
    <input type="radio" name="primary_financial_goal" value="nonfound" {if $data->primary_financial_goal eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_8_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="9" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
