 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 9</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_INVESTMENT_HORIZON}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="investment_horizon" value="< 1 Jahr" {if $data->investment_horizon eq "< 1 Jahr"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_9_1_TEXT}<br>
    <input type="radio" name="investment_horizon" value="1 -5 Jahre" {if $data->investment_horizon eq "1 -5 Jahre"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_9_2_TEXT}<br>
    <input type="radio" name="investment_horizon" value="5 - 10 Jahre" {if $data->investment_horizon eq "5 - 10 Jahre"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_9_3_TEXT}<br>
    <input type="radio" name="investment_horizon" value="> 10 Jahre" {if $data->investment_horizon eq "> 10 Jahre"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_9_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="10" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
