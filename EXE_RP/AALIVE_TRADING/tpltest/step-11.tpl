 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 11</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_ACCEPTABLE_GROWTH_TARGET}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="acceptable_growth_target" value="-2% - 5%" {if $data->acceptable_growth_target eq "-2% - 5%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_11_1_TEXT}<br>
    <input type="radio" name="acceptable_growth_target" value="-4% - 10%" {if $data->acceptable_growth_target eq "-4% - 10%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_11_2_TEXT}<br>
    <input type="radio" name="acceptable_growth_target" value="-7% - 15%" {if $data->acceptable_growth_target eq "-7% - 15%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_11_3_TEXT}<br>
    <input type="radio" name="acceptable_growth_target" value="-15% - 30%" {if $data->acceptable_growth_target eq "-15% - 30%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_11_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="12" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
